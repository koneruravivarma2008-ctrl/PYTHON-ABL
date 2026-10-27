# Program 10: Tuple and Set Operations
# Topics: tuples, sets, input/output, type conversion, loops, conditions

person = ("Ravi", 18, "CSE")
print("Tuple:", person)
print("Name:", person[0])
print("Age:", person[1])
print("Branch:", person[2])

a = set()
b = set()

count_a = int(input("How many values in set A? "))
for i in range(count_a):
    value = int(input("Enter a value for set A: "))
    a.add(value)

count_b = int(input("How many values in set B? "))
for i in range(count_b):
    value = int(input("Enter a value for set B: "))
    b.add(value)

print("Set A:", a)
print("Set B:", b)
print("Union:", a | b)
print("Intersection:", a & b)
print("A - B:", a - b)

value = int(input("Enter a value to search in set A: "))
if value in a:
    print("Present in A: Yes")
else:
    print("Present in A: No")
