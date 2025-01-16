#  If else condition

# a = int(input("Enter your age: "))
# print("Your age is:", a)

# if(a > 18):
#     print("You can drive")
# else:
#     print("You cannot drive")


# ====================================

# applePrice = 210
# budget = 200

# if(applePrice <= budget):
#     print("Alexa, add 1kg apples to the cart.")
# else:
#     print("Alexa, do not add apples to the cart.")

# ====================================
# elif statement

# num = int(input("Enter the value of num: "))

# if(num < 0):
#     print("Number is negative")
# elif(num == 0):
#     print("Number is zero.")
# elif(num == 999):
#     print("Number is special.")
# else:
#     print("Number is positive")

# ======================================
# Nested if

num = 18

if(num < 0):
    print("Number is negative")
elif(num > 0):
    if(num <= 10):
        print("Number is between 1-10")
    elif(num > 10 and num <= 20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")