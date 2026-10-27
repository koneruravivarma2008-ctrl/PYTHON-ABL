# Vowel and Consonant Counter

## Syllabus concepts
Unit II: string traversal, for loop, isalpha(), membership operator, nested if.

## 1. Problem statement
Count vowels and consonants in a line of text, ignoring digits, spaces, and punctuation.

## 2. Objectives
Traverse a string and classify alphabetic characters.

## 3. Assumptions
English letters are counted; non-letter characters are ignored.

## 4. Algorithm
1. Start.
2. Read text and convert it to lowercase.
3. Set vowel and consonant counters to zero.
4. Visit each character.
5. If it is a letter, count it as a vowel if it belongs to a, e, i, o, u; otherwise count a consonant.
6. Display both counts and stop.

## 5. Pseudocode
```text
INPUT text
vowels = 0; consonants = 0
FOR each ch in lowercase(text):
    IF ch is alphabetic:
        IF ch in 'aeiou': vowels = vowels + 1
        ELSE: consonants = consonants + 1
DISPLAY vowels, consonants
```

## 6. Flowchart
Start → Read text → Initialize counters → Visit each character → If letter, classify vowel/consonant → Display counts → Stop

Suggested symbols for a hand-drawn flowchart: oval for Start/Stop, parallelogram for input/output, rectangle for processing, and diamond for decisions.

## 7. Python source code
See [`main.py`](main.py).

## 8. Test cases and expected results
| Input | Expected result |
|---|---|
| Hello World | Vowels: 3; Consonants: 7 |
| Python 3 | Vowels: 1; Consonants: 5 |
| empty string | Vowels: 0; Consonants: 0 |

## 9. Output screenshot
Run `main.py` using one of the test cases above and add your own screenshot here before submission.

## 10. Conclusion
The program demonstrates string traversal, membership testing, and nested conditions.

---
**Student details:** Add your name, roll number, branch, and section in the final consolidated report.
