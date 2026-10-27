# Test Cases — Python ABL Projects

Use these test cases to check each program. Expected outputs below are based on the program logic; run the programs yourself to confirm and capture actual output screenshots before submission.

## 1. Simple Calculator
| # | Inputs (first, second, operator) | Expected result |
|---|---|---|
| 1 | 8, 2, + | `Result: 10.0` |
| 2 | 8, 2, - | `Result: 6.0` |
| 3 | 8, 2, * | `Result: 16.0` |
| 4 | 8, 2, / | `Result: 4.0` |
| 5 | 8, 0, / | `Error: division by zero` |
| 6 | 8, 2, % | `Invalid operator` |

## 2. Student Marks and Grade Calculator
| # | Marks (subject 1, 2, 3) | Expected result |
|---|---|---|
| 1 | 95, 85, 90 | Average: 90.0; Grade: A |
| 2 | 75, 70, 80 | Average: 75.0; Grade: C |
| 3 | 60, 60, 60 | Average: 60.0; Grade: D |
| 4 | 40, 50, 59 | Average: 49.67; Grade: F |
| 5 | 100, 100, 100 | Average: 100.0; Grade: A |
| 6 | 110, 80, 70 | `Invalid marks` |

## 3. Leap Year Checker
| # | Year | Expected result |
|---|---:|---|
| 1 | 2024 | Leap year |
| 2 | 1900 | Not a leap year |
| 3 | 2000 | Leap year |
| 4 | 2023 | Not a leap year |
| 5 | 2400 | Leap year |

## 4. Multiplication Table Generator
| # | Input | Expected result |
|---|---:|---|
| 1 | 5 | Lines from `5 x 1 = 5` through `5 x 10 = 50` |
| 2 | 0 | Ten lines with product 0 |
| 3 | -3 | Lines from `-3 x 1 = -3` through `-3 x 10 = -30` |

## 5. Factorial of a Number
| # | Input | Expected result |
|---|---:|---|
| 1 | 5 | `Factorial: 120` |
| 2 | 0 | `Factorial: 1` |
| 3 | 1 | `Factorial: 1` |
| 4 | -3 | `Factorial is not defined for negative integers` |

## 6. Palindrome String Checker
| # | Input | Expected result |
|---|---|---|
| 1 | `Level` | `It is a palindrome` |
| 2 | `nurses run` | `It is a palindrome` |
| 3 | `python` | `It is not a palindrome` |
| 4 | `Madam` | `It is a palindrome` |
| 5 | `A man, a plan, a canal: Panama` | `It is not a palindrome` (punctuation is not removed by this program) |

## 7. Vowel and Consonant Counter
| # | Input | Expected result |
|---|---|---|
| 1 | `Hello World` | Vowels: 3; Consonants: 7 |
| 2 | `Python 3` | Vowels: 1; Consonants: 5 |
| 3 | `aeiou` | Vowels: 5; Consonants: 0 |
| 4 | `123 !?` | Vowels: 0; Consonants: 0 |
| 5 | Empty line | Vowels: 0; Consonants: 0 |

## 8. Star Pattern Generator
The exact pattern depends on the prompts and implementation in `08_star_pattern/main.py`. Run the program and verify its displayed pattern for the requested row count. Include at least:
- Minimum supported row count.
- A typical row count such as 5.
- A larger row count such as 8.
- Any invalid input handling, if implemented.

## 9. List Operations and Statistics
The exact prompts and calculations depend on `09_list_statistics/main.py`. Test with:
- A list containing positive integers, such as `4, 2, 8, 6`.
- A list containing duplicate values, such as `3, 3, 1, 5`.
- A list containing negative and positive values, such as `-2, 0, 7`.
- The smallest valid list size and any empty-list/invalid-input handling, if implemented.

Check the displayed list, sorted order, minimum, maximum, sum, and average where those operations are provided.

## 10. Tuple and Set Operations
The exact prompts and values depend on `10_tuple_set_operations/main.py`. Test with:
- Tuples containing distinct values.
- Tuples with repeated values.
- Two sets with overlapping elements, such as A = {1, 2, 3} and B = {3, 4, 5}.
- Two disjoint sets.
- Membership tests for an item that is present and one that is absent.

Check the tuple output and set union, intersection, difference, and membership operations where provided.

## Screenshot checklist
For each of the 10 programs:
1. Open a terminal in the corresponding project folder.
2. Run `python main.py` (or `python3 main.py`).
3. Enter one of the test cases above.
4. Capture the actual terminal showing the program name, input, and output.
5. Save screenshots with clear names, for example `01_calculator_test1.png`.
6. Do not use mock or edited output as proof of execution; screenshots should show real runs.

**Note:** This file lists test cases and expected results. It does not claim that every test has already been executed or screenshot-captured.
