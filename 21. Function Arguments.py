# Function arguments

def average(a, b):
    print("The average is ", (a+b)/2)

# average(1, 5)

# ===========================

def average(a = 9, b = 1):
    print("The average is ", (a + b)/ 2)

# average()
# average(b=3)
# average(1, 5)
# average(a=4, b=12)

# =============================

def average(*numbers):
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
    print("Average is ", sum/len(numbers))

# average(5, 6, 7, 1)
# =================================

def names(**name):
    print(type(name))
    print("hello,", name["fname"], name['mname'], name["lname"])

names(mname="Buchanan", lname = "Barnes", fname = "James")