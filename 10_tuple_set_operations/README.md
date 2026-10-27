# Tuple and Set Operations

## Syllabus concepts
Unit III: tuple creation and unpacking, sets, membership testing, union, intersection, and difference.

## 1. Problem statement
Create a tuple, unpack its values, accept two sets of integers, and demonstrate basic set operations.

## 2. Objectives
- Understand that tuples are ordered and immutable.
- Practice tuple unpacking.
- Use sets to store unique values.
- Perform union, intersection, difference, and membership testing.

## 3. Assumptions
Set values are integers separated by spaces. Duplicate values are automatically removed by a set.

## 4. Algorithm
1. Start.
2. Create a tuple with a name, age, and branch.
3. Unpack the tuple into three variables.
4. Read two groups of integers and convert each group into a set.
5. Display the tuple and unpacked values.
6. Display union, intersection, and difference.
7. Read a value and check whether it belongs to set A.
8. Stop.

## 5. Pseudocode
```text
person = (name, age, branch)
name, age, branch = person
INPUT values for set A and set B
A = set(values A)
B = set(values B)
DISPLAY person and unpacked values
DISPLAY A union B
DISPLAY A intersection B
DISPLAY A difference B
INPUT value
DISPLAY value in A
```

## 6. Flowchart
Start → Create and unpack tuple → Read values for sets A and B → Create sets → Display union, intersection, and difference → Read search value → Test membership → Stop.

For a hand-drawn flowchart, use an oval for Start/Stop, parallelograms for input/output, rectangles for processing, and a diamond for a decision.

## 7. Python source code
See [`main.py`](main.py).

## 8. Test cases and expected results
| Set A | Set B | Search value | Expected result |
|---|---|---:|---|
| 1 2 3 | 3 4 | 2 | Union contains 1, 2, 3, 4; intersection contains 3; A - B contains 1, 2; membership is True |
| 5 | 6 | 7 | Union contains 5, 6; intersection is empty; A - B contains 5; membership is False |

Note: Set display order may vary in Python.

## 9. Output screenshot
Run `main.py` with one of the test cases above and insert your own screenshot of the actual output before submission.

## 10. Conclusion
The program demonstrates tuple unpacking, set uniqueness, set operations, and membership testing.

---
**Student details:** Add your name, roll number, branch, and section to the final consolidated report.
