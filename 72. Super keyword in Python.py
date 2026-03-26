# Super keyword in Python

'''
The super() keyword in Python is used to refer the parent class. It is 
especially useful when a class inherits from multiple parent class and 
you want to call a method from one of the parent classes.

When a class inherits from a parent class, it can override or extend
the methods defined in the parent class. However, sometimes you might
want to use the parent class method in the child class. This is where 
the super() keyword comes in handy.
'''

# class ParentClass:
#     def parent_method(self):
#         print("This is the parent method.")


# class ChildClass(ParentClass):
#     def child_method(self):
#         print("This is the child method")
#         super().parent_method()

# child_object = ChildClass()
# child_object.child_method()

# ==============================================

# class ParentClass:
#     def parent_method(self):
#         print("This is the parent method")

# class ChildClass(ParentClass):
#     def parent_method(self):
#         print("harry")
#         super().parent_method()

#     def child_method(self):
#         print("This is the child method")
#         super().parent_method()

# child_object = ChildClass()
# child_object.parent_method()
# child_object.child_method()

# ================================================

# class Employee:
#     def __init__(self, name, id):
#         self.name = name
#         self.id = id

    
# class Programmer:
#     def __init__(self, name, id, lang):
#         self.name = name
#         self.id = id
#         self.lang = lang

# rohan = Employee("Rohan Das", "420")
# harry = Programmer("Harry", "2345", "Python")
# print(rohan.name)

# ================================================

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    
class Programmer(Employee):
    def __init__(self, name, id, lang):
        self.lang = lang
        super().__init__(name, id)

rohan = Employee("Rohan Das", "420")
harry = Programmer("Harry", "2345", "Python")
print(rohan.name)
print(harry.name)
print(harry.id)
print(harry.lang)