# List Operations and Statistics

## Syllabus concepts
Unit III: list creation, traversal, append(), len(), sum(), min(), max().

## 1. Problem statement
Read integers into a list and display the list, sum, average, minimum, and maximum.

## 2. Objectives
Practice list creation, traversal, appending elements, and common aggregate operations.

## 3. Assumptions
The user enters at least one integer separated by spaces. An empty input is handled.

## 4. Algorithm
1. Start.
2. Read space-separated values.
3. Convert each value to an integer and append it to a list.
4. If the list is empty, display a message.
5. Otherwise calculate sum, average, minimum, and maximum.
6. Display the results and stop.

## 5. Pseudocode
```text
INPUT space-separated values
numbers = empty list
FOR each value: append integer(value) to numbers
IF list is empty: DISPLAY no values
ELSE: calculate sum, average, min, max; DISPLAY results
```

## 6. Flowchart
Start → Read values → Convert and append to list → Is list empty? → Calculate statistics → Display results → Stop

Suggested symbols for a hand-drawn flowchart: oval for Start/Stop, parallelogram for input/output, rectangle for processing, and diamond for decisions.

## 7. Python source code
See [`main.py`](main.py).

## 8. Test cases and expected results
| Input | Expected result |
|---|---|
| 2 4 6 | List: [2, 4, 6]; Sum: 12; Average: 4.0; Minimum: 2; Maximum: 6 |
| 7 | Sum: 7; Average: 7.0; Minimum: 7; Maximum: 7 |

## 9. Output screenshot
Run `main.py` using one of the test cases above and add your own screenshot here before submission.

## 10. Conclusion
The program demonstrates list creation, traversal, and basic statistical operations.

---
**Student details:** Add your name, roll number, branch, and section in the final consolidated report.
