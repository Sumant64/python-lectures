# Class Methods as Alternative Constructors

'''
Sometimes we use class methods to use as a constructors
'''

# Normal class
# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

# e = Employee("Harry", 12000)
# print(e.name)
# print(e.salary)

# string = "Harry-12000"
# e = Employee(string.split("-")[0], string.split("-")[1])
# print(e.name)
# print(e.salary)

# =====================================================

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def fromStr(cls, string):
        return cls(string.split("-")[0], string.split("-")[1])
    
e1 = Employee("Harry", 12000)
print(e1.name)
print(e1.salary)

string = "John-12000"
e2 = Employee.fromStr(string)
print(e2.name)
print(e2.salary)