# Student Marks and Grade Calculator

## Syllabus concepts
Unit I: arithmetic and relational operators; Unit II: if-elif-else and logical operators.

## 1. Problem statement
Accept marks in three subjects, calculate the average, and display a grade.

## 2. Objectives
Practice arithmetic, validation, relational operators, and an if-elif-else ladder.

## 3. Assumptions
Marks must be between 0 and 100. Grades: A ≥ 90, B ≥ 80, C ≥ 70, D ≥ 60, otherwise F.

## 4. Algorithm
1. Start.
2. Read three subject marks.
3. Check that all marks are between 0 and 100.
4. Calculate the average.
5. Select a grade using if-elif-else.
6. Display the average and grade.
7. Stop.

## 5. Pseudocode
```text
INPUT m1, m2, m3
IF any mark is outside 0..100: DISPLAY invalid marks
ELSE:
    average = (m1 + m2 + m3) / 3
    IF average >= 90: grade = A
    ELSE IF average >= 80: grade = B
    ELSE IF average >= 70: grade = C
    ELSE IF average >= 60: grade = D
    ELSE: grade = F
    DISPLAY average, grade
```

## 6. Flowchart
Start → Read three marks → Validate range → Calculate average → Grade decision ladder → Display average and grade → Stop

Suggested symbols for a hand-drawn flowchart: oval for Start/Stop, parallelogram for input/output, rectangle for processing, and diamond for decisions.

## 7. Python source code
See [`main.py`](main.py).

## 8. Test cases and expected results
| Input | Expected result |
|---|---|
| 95, 85, 90 | Average: 90.0; Grade: A |
| 75, 70, 80 | Average: 75.0; Grade: C |
| 110, 80, 70 | Invalid marks |

## 9. Output screenshot
Run `main.py` using one of the test cases above and add your own screenshot here before submission.

## 10. Conclusion
The program calculates an average and classifies it using conditional statements.

---
**Student details:** Add your name, roll number, branch, and section in the final consolidated report.
