# Project 1: Simple Calculator

## Problem statement
Write a Python program that accepts two numbers and an arithmetic operator, performs the selected operation, and displays the result.

## Objectives
- Practise variables and numeric input.
- Use type conversion with `float()`.
- Apply arithmetic and relational operators.
- Use `if`, `elif`, and `else` decision statements.
- Handle division by zero safely.

## Assumptions
- The user enters valid numeric values.
- The operator must be one of `+`, `-`, `*`, or `/`.
- Division by zero is not permitted.

## Algorithm
1. Start.
2. Input the first number.
3. Input the second number.
4. Input the arithmetic operator.
5. If the operator is `+`, add the numbers.
6. Else if the operator is `-`, subtract the second number from the first.
7. Else if the operator is `*`, multiply the numbers.
8. Else if the operator is `/`, check whether the second number is zero.
9. If it is zero, display a division-by-zero error; otherwise divide the numbers.
10. If the operator is not valid, display an invalid-operator message.
11. Stop.

## Pseudocode
```text
START
INPUT a
INPUT b
INPUT operator

IF operator == "+" THEN
    DISPLAY a + b
ELSE IF operator == "-" THEN
    DISPLAY a - b
ELSE IF operator == "*" THEN
    DISPLAY a * b
ELSE IF operator == "/" THEN
    IF b == 0 THEN
        DISPLAY "Error: division by zero"
    ELSE
        DISPLAY a / b
    END IF
ELSE
    DISPLAY "Invalid operator"
END IF

STOP
```

## Flowchart guide
Draw the flowchart using these nodes in order:

1. **Oval:** Start
2. **Parallelogram:** Input `a`, `b`, and operator
3. **Diamond:** Is operator `+`? — Yes → **Parallelogram:** Display `a + b`; No → next decision
4. **Diamond:** Is operator `-`? — Yes → display `a - b`; No → next decision
5. **Diamond:** Is operator `*`? — Yes → display `a * b`; No → next decision
6. **Diamond:** Is operator `/`? — Yes → check `b == 0`; No → display invalid operator
7. **Diamond:** Is `b == 0`? — Yes → display division-by-zero error; No → display `a / b`
8. **Oval:** Stop

Connect each No branch to the next operator decision and all result/error branches to Stop.

## Conclusion
This program demonstrates basic input/output, type conversion, arithmetic operators, conditional statements, and error checking.
