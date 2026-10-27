# Program 9: List Operations and Statistics
# Topics: input/output, type conversion, lists, for loop, conditions

count = int(input("How many numbers do you want to enter? "))
numbers = []

if count <= 0:
    print("Please enter a positive count")
else:
    for i in range(count):
        value = int(input("Enter a number: "))
        numbers.append(value)

    total = 0
    smallest = numbers[0]
    largest = numbers[0]

    for value in numbers:
        total = total + value

        if value < smallest:
            smallest = value

        if value > largest:
            largest = value

    average = total / count

    print("List:", numbers)
    print("Sum:", total)
    print("Average:", average)
    print("Minimum:", smallest)
    print("Maximum:", largest)
