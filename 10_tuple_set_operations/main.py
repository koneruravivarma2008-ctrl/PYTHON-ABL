# Program 10: Tuple and Set Operations

person = ("Ravi", 18, "CSE")
name, age, branch = person

a = set(map(int, input("Enter set A values separated by spaces: ").split()))
b = set(map(int, input("Enter set B values separated by spaces: ").split()))

print("Tuple:", person)
print("Unpacked:", name, age, branch)
print("Union:", a | b)
print("Intersection:", a & b)
print("A - B:", a - b)

value = int(input("Enter a value to search in set A: "))
print("Present in A:", value in a)
