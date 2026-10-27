# Program 8: Right-Angled Star Pattern
# Topics: input/output, type conversion, nested for loops, pattern generation

rows = int(input("Enter number of rows: "))

if rows <= 0:
    print("Enter a positive number of rows")
else:
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print("*", end="")
        print()
