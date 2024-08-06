def number_to_binary(x):
    if 1 <= x <= 255:
        binary = format(x, '08b')
        print(" t   he number you entered in binary code is {}".format(binary))
        return binary
    else:
        print ("Your input isn't valid please enter a number between 1 and 255")
        return None

num = int(input("Please enter the number you want to convert to binary code: "))
binary = number_to_binary(num)

binary_list = [int(bit) for bit in binary]
print(binary_list)

for i in range (len(binary_list)): #complement to one
    if binary_list[i] == 1:
        binary_list[i] = 0
    else:
        binary_list[i] = 1

#comlement to two 
carry = 1
for y in range (len(binary_list) -1, -1, -1):
    if binary_list[y] == 1 and carry == 1:
        binary_list[y] = 0
    else:
        binary_list[y] += carry
        carry = 0

print("The binary code of the number you entered in the complement to two's method is {}".format(binary_list))

        
        
        



