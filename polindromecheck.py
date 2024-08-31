def polindrome_check(word):
    if word == word[::-1]:
        print(f"The word {word} is a polindrome")
    else:
        print(f"The word {word} isn't a polindrome")

input_word = input("Please enter a word to check if its a polindrome")
polindrome_check(input_word)