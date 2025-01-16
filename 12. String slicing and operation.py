# String slicing and operations

names = "Harry, Shubham"
print(names[0:])
print(names[0:5])
print(len(names))

# Negative index slicing
fruit = "Mango"
print(fruit[0: -3]) # -3 index means len(names) - 3 = 2
print(fruit[0: len(fruit) - 3])
print(fruit[: len(fruit) - 3])