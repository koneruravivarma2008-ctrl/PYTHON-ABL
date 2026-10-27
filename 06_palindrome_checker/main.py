# Program 6: Palindrome String Checker

text = input("Enter a word or phrase: ")
clean_text = text.lower().replace(" ", "")
reversed_text = clean_text[::-1]

if clean_text == reversed_text:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
