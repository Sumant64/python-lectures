# Access Modifiers in python

'''
Access Specifiers/ Modifiers
o Access specifiers or access modifiers in python programming are used to
  limit the access of class variables and class methods outside of class
  while implementing the concepts of inheritance.

Types of access specifiers:
1. Public access modifier
2. Private access modifier
3. Protected access modifier
'''


class Employee:
    def __init__(self):
        self.__name = "Harry" #used as private variable

a = Employee()
# print(a.__name) #cannot be accessed, it will give error

# to access the private variable we need to write
print(a._Employee__name)

# We can see all the methods of class by __dir__()
print(a.__dir__())

'''
['_Employee__name', '__module__', '__init__', '__dict__', 
'__weakref__', '__doc__', '__new__', '__repr__', '__hash__', 
'__str__', '__getattribute__', '__setattr__', '__delattr__', 
'__lt__', '__le__', '__eq__', '__ne__', '__gt__', '__ge__', 
'__reduce_ex__', '__reduce__', '__getstate__', '__subclasshook__', 
'__init_subclass__', '__format__', '__sizeof__', '__dir__', '__class__']
'''

# ==========================================================
# Protected 

class Student:
    def __init__(self):
        self._name = "Harry"

    def _funName(self): #protected
        return "CodeWithHarry"
    
class Subject(Student): #inherited class
    pass

obj = Student()
obj1 = Subject()

# Calling by object of Student clas
print(obj._funName())
print(obj._name)