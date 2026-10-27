# Program 6: Palindrome String Checker
# Topics: input/output, strings, conditions, while loop

word = input("Enter a word: ")
word = word.lower()

reversed_word = ""
i = len(word) - 1

while i >= 0:
    reversed_word = reversed_word + word[i]
    i = i - 1

if word == reversed_word:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
