# Program 2: Student Marks and Grade Calculator

m1 = int(input("Enter marks for subject 1 (0-100): "))
m2 = int(input("Enter marks for subject 2 (0-100): "))
m3 = int(input("Enter marks for subject 3 (0-100): "))

if not (0 <= m1 <= 100 and 0 <= m2 <= 100 and 0 <= m3 <= 100):
    print("Invalid marks")
else:
    average = (m1 + m2 + m3) / 3

    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    elif average >= 60:
        grade = "D"
    else:
        grade = "F"

    print("Average:", round(average, 2))
    print("Grade:", grade)
