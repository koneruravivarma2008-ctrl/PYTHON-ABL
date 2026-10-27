# Program 3: Leap Year Checker
# Topics: input/output, type conversion, operators, if-elif-else

year = int(input("Enter a year: "))

if year % 400 == 0:
    print(year, "is a leap year")
elif year % 100 == 0:
    print(year, "is not a leap year")
elif year % 4 == 0:
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")
