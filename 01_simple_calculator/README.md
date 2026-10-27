# Simple Calculator

## Syllabus concepts
Unit I: input/output, type conversion, arithmetic operators, decision statements.

## 1. Problem statement
Read two numbers and an arithmetic operator, then display the calculated result.

## 2. Objectives
Practice variables, float conversion, arithmetic operators, and if-elif-else.

## 3. Assumptions
The user enters numeric values and one of +, -, *, or /. Division by zero is checked.

## 4. Algorithm
1. Start.
2. Read two numbers and an operator.
3. Use if-elif to select the operation.
4. For division, check that the second number is not zero.
5. Display the result or an error message.
6. Stop.

## 5. Pseudocode
```text
INPUT a, b, operator
IF operator == '+': result = a + b
ELSE IF operator == '-': result = a - b
ELSE IF operator == '*': result = a * b
ELSE IF operator == '/':
    IF b == 0: DISPLAY error
    ELSE: DISPLAY a / b
ELSE: DISPLAY invalid operator
```

## 6. Flowchart
Start → Read two numbers and operator → Select operation → Check division by zero if needed → Display result/error → Stop

Suggested symbols for a hand-drawn flowchart: oval for Start/Stop, parallelogram for input/output, rectangle for processing, and diamond for decisions.

## 7. Python source code
See [`main.py`](main.py).

## 8. Test cases and expected results
| Input | Expected result |
|---|---|
| 8, 2, + | Result: 10.0 |
| 8, 2, / | Result: 4.0 |
| 8, 0, / | Error: division by zero |

## 9. Output screenshot
Run `main.py` using one of the test cases above and add your own screenshot here before submission.

## 10. Conclusion
The program demonstrates basic arithmetic operators and conditional statements.

---
**Student details:** Add your name, roll number, branch, and section in the final consolidated report.
