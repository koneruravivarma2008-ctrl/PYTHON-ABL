# Leap Year Checker

## Syllabus concepts
Unit I: relational and logical operators; Unit II: nested if / elif conditions.

## 1. Problem statement
Determine whether a year entered by the user is a leap year.

## 2. Objectives
Apply divisibility rules using arithmetic and decision statements.

## 3. Assumptions
The input is a positive whole-number year in the Gregorian calendar.

## 4. Algorithm
1. Start.
2. Read the year.
3. If divisible by 400, it is a leap year.
4. Otherwise, if divisible by 100, it is not a leap year.
5. Otherwise, if divisible by 4, it is a leap year.
6. Otherwise, it is not a leap year.
7. Display the result and stop.

## 5. Pseudocode
```text
INPUT year
IF year % 400 == 0: leap year
ELSE IF year % 100 == 0: not leap year
ELSE IF year % 4 == 0: leap year
ELSE: not leap year
DISPLAY result
```

## 6. Flowchart
Start → Read year → Check divisibility by 400 → Check by 100 → Check by 4 → Display result → Stop

Suggested symbols for a hand-drawn flowchart: oval for Start/Stop, parallelogram for input/output, rectangle for processing, and diamond for decisions.

## 7. Python source code
See [`main.py`](main.py).

## 8. Test cases and expected results
| Input | Expected result |
|---|---|
| 2024 | 2024 is a leap year |
| 1900 | 1900 is not a leap year |
| 2000 | 2000 is a leap year |

## 9. Output screenshot
Run `main.py` using one of the test cases above and add your own screenshot here before submission.

## 10. Conclusion
The program checks leap years using the modulus operator and conditional logic.

---
**Student details:** Add your name, roll number, branch, and section in the final consolidated report.
