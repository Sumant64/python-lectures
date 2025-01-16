# Decorators in python

# Decorator function
# def greet(fx): 
#     def mfx():
#         print("Good morning")
#         fx()
#         print("Thanks for using this function")
#     return mfx


# @greet
# def hello():
#     print("hello world")

# hello()

# ==================================
# Calling hello as a normal way
# def hello():
#     print("hello world")


# greet(hello)()

# ========================================
# function with arguments (We need to provide arguments in greet decorator)

def greet(fx): 
    def mfx(*args, **kwargs):
        print("Good morning")
        fx(*args, **kwargs)
        print("Thanks for using this function")
    return mfx

@greet
def add(a, b):
    print(a + b)

add(10, 20)