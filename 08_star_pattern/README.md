# Star Pattern Generator

## Syllabus concepts
Unit II: nested for loops and pattern generation.

## 1. Problem statement
Print a right-angled triangle of stars for a user-specified number of rows.

## 2. Objectives
Understand nested loops and how loop counts produce patterns.

## 3. Assumptions
The number of rows should be a positive integer.

## 4. Algorithm
1. Start.
2. Read the number of rows.
3. If rows is not positive, display a message.
4. For each row i from 1 through rows, print i stars.
5. Move to a new line after each row.
6. Stop.

## 5. Pseudocode
```text
INPUT rows
IF rows <= 0: DISPLAY error
ELSE:
    FOR i from 1 to rows:
        FOR j from 1 to i: PRINT '*' without newline
        PRINT newline
```

## 6. Flowchart
Start → Read row count → Validate positive count → Outer loop for rows → Inner loop prints stars → New line → Stop

Suggested symbols for a hand-drawn flowchart: oval for Start/Stop, parallelogram for input/output, rectangle for processing, and diamond for decisions.

## 7. Python source code
See [`main.py`](main.py).

## 8. Test cases and expected results
| Input | Expected result |
|---|---|
| 4 | * / ** / *** / **** on separate lines |
| 1 | * |
| 0 | Enter a positive number of rows |

## 9. Output screenshot
Run `main.py` using one of the test cases above and add your own screenshot here before submission.

## 10. Conclusion
The program demonstrates nested iteration for simple pattern generation.

---
**Student details:** Add your name, roll number, branch, and section in the final consolidated report.
