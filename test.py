import sys
from collections import Counter 

def main():
    if len(sys.argv) != 3:
        print("Missing variable")
        sys.exit(1)
    file_name = sys.argv[1]
    try:
       N = int(sys.argv[2])
    except ValueError:
       print("N should be an integer")
       sys.exit(1)

    try:
       with open(file_name, 'r') as file:
          file_content = file.read()
    except FileNotFoundError:
       print(f"the file {file_name} was not found")
       sys.exit(1)


    list_content = file_content.split() # spliting the file's content into a list
    content_count = {} # Creating a dictionaray to store the each word and the amount of it in the list

    # Placing each word in the dictionary and the amount of it in the list
    content_count = Counter(list_content)

    # Sort the dictionary by values 
    sorted_content = sorted(content_count.items(), key=lambda item: item[1], reverse=True)
    
    for word, count in sorted_content[:N]:
       print(f"{word}: {count}")

if __name__ == "__main__":
    main()         
