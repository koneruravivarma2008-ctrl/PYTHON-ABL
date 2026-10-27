# Program 2: Student Marks and Grade Calculator
# Topics: input/output, type conversion, arithmetic operators, conditions

m1 = int(input("Enter marks for subject 1 (0-100): "))
m2 = int(input("Enter marks for subject 2 (0-100): "))
m3 = int(input("Enter marks for subject 3 (0-100): "))

if m1 < 0 or m1 > 100 or m2 < 0 or m2 > 100 or m3 < 0 or m3 > 100:
    print("Invalid marks")
else:
    total = m1 + m2 + m3
    average = total / 3
    print("Average:", average)

    if average >= 90:
        print("Grade: A")
    elif average >= 80:
        print("Grade: B")
    elif average >= 70:
        print("Grade: C")
    elif average >= 60:
        print("Grade: D")
    else:
        print("Grade: F")
