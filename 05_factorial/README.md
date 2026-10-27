# Factorial of a Number

## Syllabus concepts
Unit II: while loop, conditions, assignment and arithmetic operators.

## 1. Problem statement
Calculate the factorial of a non-negative integer using a while loop.

## 2. Objectives
Practice loop control and an accumulator variable.

## 3. Assumptions
The input is an integer. Negative values are rejected and 0! equals 1.

## 4. Algorithm
1. Start.
2. Read n.
3. If n is negative, display an error.
4. Otherwise set factorial = 1 and i = 1.
5. While i ≤ n, multiply factorial by i and increment i.
6. Display factorial and stop.

## 5. Pseudocode
```text
INPUT n
IF n < 0: DISPLAY error
ELSE:
    factorial = 1; i = 1
    WHILE i <= n:
        factorial = factorial * i
        i = i + 1
    DISPLAY factorial
```

## 6. Flowchart
Start → Read n → Is n negative? → Yes: display error / No: initialize → While i ≤ n update factorial and i → Display result → Stop

Suggested symbols for a hand-drawn flowchart: oval for Start/Stop, parallelogram for input/output, rectangle for processing, and diamond for decisions.

## 7. Python source code
See [`main.py`](main.py).

## 8. Test cases and expected results
| Input | Expected result |
|---|---|
| 5 | Factorial: 120 |
| 0 | Factorial: 1 |
| -3 | Factorial is not defined for negative integers |

## 9. Output screenshot
Run `main.py` using one of the test cases above and add your own screenshot here before submission.

## 10. Conclusion
The program demonstrates while-loop repetition and updating a running product.

---
**Student details:** Add your name, roll number, branch, and section in the final consolidated report.
