# Program 9: List Operations and Statistics

values = input("Enter integers separated by spaces: ").split()
numbers = []

for value in values:
    numbers.append(int(value))

if len(numbers) == 0:
    print("No numbers entered")
else:
    total = sum(numbers)
    average = total / len(numbers)
    print("List:", numbers)
    print("Sum:", total)
    print("Average:", round(average, 2))
    print("Minimum:", min(numbers))
    print("Maximum:", max(numbers))
