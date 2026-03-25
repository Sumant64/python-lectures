# dir, __dict__ and help in python

# dir
'''
o The dir() function returns a list of all the attributes and methods
  (including dundler methods) available for an object. It is a 
  useful tool for discovering what you can do with an object.
'''

x = [1, 2, 3]
# print(dir(x))
# print(x.__add__) # <method-wrapper '__add__' of list object at 0x000002131365B740>

#=====================================================
# __dict__

'''
The __dict__ attribute
The __dict__ attribute returns a dictionary representationof an object's
attribute. It is a useful tool for introspection.
'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    
p = Person("John", 30)
# print(p.__dict__)

# ========================================================
# help()

'''
The help() function is used to get help documentation for an object,
including a description of its attribute and methods.
'''

print(help(str))

'''
Output
class str(object)
 |  str(object='') -> str
 |  str(bytes_or_buffer[, encoding[, errors]]) -> str
 |
 |  Create a new string object from the given object. If encoding or
 |  errors is specified, then the object must expose a data buffer
 |  that will be decoded using the given encoding and error handler.
 |  Otherwise, returns the result of object.__str__() (if defined)
 |  or repr(object).

 more info...
'''