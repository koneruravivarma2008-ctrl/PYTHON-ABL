# Palindrome String Checker

## Syllabus concepts
Unit II: strings, lower(), replace(), slicing, if-else.

## 1. Problem statement
Check whether a word or phrase reads the same forward and backward, ignoring spaces and letter case.

## 2. Objectives
Practice string methods, slicing, and equality comparison.

## 3. Assumptions
Spaces and letter case are ignored. Punctuation is not removed.

## 4. Algorithm
1. Start.
2. Read a string.
3. Convert it to lowercase and remove spaces.
4. Reverse the normalized string using slicing.
5. Compare the string with its reverse.
6. Display the result and stop.

## 5. Pseudocode
```text
INPUT text
clean = lowercase(text) with spaces removed
reversed_text = reverse(clean)
IF clean == reversed_text: DISPLAY palindrome
ELSE: DISPLAY not palindrome
```

## 6. Flowchart
Start → Read text → Lowercase and remove spaces → Reverse text → Compare → Display result → Stop

Suggested symbols for a hand-drawn flowchart: oval for Start/Stop, parallelogram for input/output, rectangle for processing, and diamond for decisions.

## 7. Python source code
See [`main.py`](main.py).

## 8. Test cases and expected results
| Input | Expected result |
|---|---|
| Level | It is a palindrome |
| nurses run | It is a palindrome |
| python | It is not a palindrome |

## 9. Output screenshot
Run `main.py` using one of the test cases above and add your own screenshot here before submission.

## 10. Conclusion
The program demonstrates string normalization, slicing, and conditional comparison.

---
**Student details:** Add your name, roll number, branch, and section in the final consolidated report.
