# Magic/Dunder Methods in Python

'''
-> Magic/Dunder Methods in Python
-----------------------------------
o These are special methods that you can define in your classes, 
and when invoked, they give you a powerful way to manipulate objects and 
their behaviour.

o Magic methods, also known as "dunders" from the double underscores
surrounding their names, are powerful tools that allow you to customize the 
behaviour of your classes. They are used to implement special methods such as 
the addition, substraction and comparison operators, as well as some more 
advanced techniques like description and properties.

ex. __init__, __str__, __repr__
'''

# ==============================================
# __init__ method

'''
The init method is a special method that is automatically invoked 
when you create a new instance of a class. This method is responsible
for setting up the object's initial state, and it is where you would
typically define any instance variables that you need.
'''

# class Employee:
#     def __init__(self, name):
#         self.name = name

#     def __len__(self):
#         i = 0
#         for c in self.name:
#             i = i + 1
#         return i


# e = Employee("Harry")
# print(e.name)
# print(len(e))

# =============================================
# __str__ and __repr__ methods

'''
The str and repr methods are both used to convert an object to a string
representation. The str method is used when you want to print out
an object, while the repr method is used when you want to get a string
representation of an object that can be used to recreate the object.
'''

# __len__ method
'''
The len method is used to get the length of an object. This is useful
when you want to be able to find the size of a data structure, such as a
list or dictionary.
'''

# class Employee:
#     def __init__(self, name):
#         self.name = name

#     def __len__(self):
#         i = 0
#         for c in self.name:
#             i = i + 1
#         return i

#     def __str__(self):
#         return f"The name of the employee is {self.name} str"
    
#     def __repr__(self):
#         return f"The name of the employee is {self.name} repr"


# e = Employee("harry")
# print(e) # it will print the str method, if str is not there then it will print the repr

# print(str(e))
# print(repr(e))

# ========================================================
# Call method

'''
__call__ method
o The call method is used to make an object callable, meaning that you can
pass it as a parameter to a function and it will be executed when the function is 
called. This is an incredibly powerful tool that allows you to create objects
that behave like functions.

o There are just a few of the many magic methods available in Python.
They are incredibly powerful tools that allow you to customize the 
behaviour of your objects, and can make your code much cleaner and 
easier to understand.
'''

class Employee:
    def __init__(self, name):
        self.name = name

    def __len__(self):
        i = 0
        for c in self.name:
            i = i + 1
        return i

    def __str__(self):
        return f"The name of the employee is {self.name} str"
    
    def __repr__(self):
        return f"The name of the employee is {self.name} repr"
    
    def __call__(self):
        print("Hey I am good")


e = Employee("harry")
e() # __call__ will directly call the object just like function