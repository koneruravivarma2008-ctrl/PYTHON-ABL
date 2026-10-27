# Test Cases — Python ABL Projects

Run these cases against the source code in each project folder. Expected results below are derived from the current code; capture actual terminal output after running each program.

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
| 1 | 5 | From `5 x 1 = 5` through `5 x 10 = 50` |
| 2 | 0 | Ten lines with product 0 |
| 3 | -3 | From `-3 x 1 = -3` through `-3 x 10 = -30` |

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
| 5 | `A man, a plan, a canal: Panama` | `It is not a palindrome` because punctuation is retained |

## 7. Vowel and Consonant Counter
| # | Input | Expected result |
|---|---|---|
| 1 | `Hello World` | Vowels: 3; Consonants: 7 |
| 2 | `Python 3` | Vowels: 1; Consonants: 5 |
| 3 | `aeiou` | Vowels: 5; Consonants: 0 |
| 4 | `123 !?` | Vowels: 0; Consonants: 0 |
| 5 | Empty line | Vowels: 0; Consonants: 0 |

## 8. Right-Angled Star Pattern
| # | Input rows | Expected result |
|---|---:|---|
| 1 | 1 | One line: `*` |
| 2 | 3 | Lines: `*`, `**`, `***` |
| 3 | 5 | Five lines, one through five stars |
| 4 | 0 | `Enter a positive number of rows` |
| 5 | -2 | `Enter a positive number of rows` |

## 9. List Operations and Statistics
| # | Input integers (space-separated) | Expected result |
|---|---|---|
| 1 | `4 2 8 6` | List: [4, 2, 8, 6]; Sum: 20; Average: 5.0; Minimum: 2; Maximum: 8 |
| 2 | `3 3 1 5` | List: [3, 3, 1, 5]; Sum: 12; Average: 3.0; Minimum: 1; Maximum: 5 |
| 3 | `-2 0 7` | Sum: 5; Average: 1.67; Minimum: -2; Maximum: 7 |
| 4 | Empty line | `No numbers entered` |

## 10. Tuple and Set Operations
The tuple is fixed in the program as `('Ravi', 18, 'CSE')`. For each set test, enter the two sets and then the search value.

| # | Set A | Set B | Search value | Expected result |
|---|---|---|---:|---|
| 1 | `1 2 3` | `3 4 5` | 2 | Union contains 1,2,3,4,5; intersection contains 3; A - B contains 1,2; Present in A: True |
| 2 | `1 2` | `4 5` | 9 | Union contains 1,2,4,5; intersection is empty; A - B contains 1,2; Present in A: False |
| 3 | `1 1 2` | `2 2 3` | 3 | Duplicates collapse in sets; union contains 1,2,3; intersection contains 2; Present in A: False |

**Note:** Python may display set elements in a different order. Compare set membership, not the printed ordering.

## Screenshot checklist
For every program, run `python main.py` (or `python3 main.py`) in its project folder and capture the real terminal showing the input and output. Use names such as `01_calculator_test1.png`. Do not present fabricated or edited output as proof of execution.

This document lists test cases and expected results; it does not claim that all cases have already been executed or that screenshots have been captured.
