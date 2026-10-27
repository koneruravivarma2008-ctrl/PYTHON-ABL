# Program 5: Factorial of a Number
# Topics: input/output, type conversion, while loop, arithmetic operators, conditions

n = int(input("Enter a non-negative integer: "))

if n < 0:
    print("Factorial is not defined for negative integers")
else:
    factorial = 1
    i = 1

    while i <= n:
        factorial = factorial * i
        i = i + 1

    print("Factorial:", factorial)
