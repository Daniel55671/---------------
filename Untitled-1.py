import sys
from collections import Counter

def main():
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 3:
        print("Usage: python script.py <file_name> <N>")
        sys.exit(1)

    file_name = sys.argv[1]

    # Convert N to an integer and handle ValueError
    try:
        N = int(sys.argv[2])
    except ValueError:
        print("N should be an integer.")
        sys.exit(1)

    # Read the file and handle FileNotFoundError
    try:
        with open(file_name, 'r') as file:
            file_content = file.read()
    except FileNotFoundError:
        print(f"The file '{file_name}' was not found.")
        sys.exit(1)

    # Split the file's content into a list of words
    list_content = file_content.split()

    # Count the occurrences of each word
    content_count = Counter(list_content)

    # Sort the dictionary by values in descending order
    sorted_content = sorted(content_count.items(), key=lambda item: item[1], reverse=True)
    
    # Print the top N words and their counts
    for word, count in sorted_content[:N]:
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()
