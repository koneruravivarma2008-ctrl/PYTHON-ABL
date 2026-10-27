# Program 7: Vowel and Consonant Counter
# Topics: input/output, strings, for loop, conditions, counters

text = input("Enter a line of text: ")
text = text.lower()
vowels = 0
consonants = 0

for ch in text:
    if ch in "abcdefghijklmnopqrstuvwxyz":
        if ch in "aeiou":
            vowels = vowels + 1
        else:
            consonants = consonants + 1

print("Vowels:", vowels)
print("Consonants:", consonants)
