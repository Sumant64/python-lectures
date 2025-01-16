# Static Method in python

'''
o Static methods in python are methods that belong to a class rather than
  an instance of the class. They are defined using the @staticmethod
  decorator and do not have access to the instance of the class (i.e. self).
  They are called on the class itself, not on an instance of the class.
  Static methods are often used to create utility functions that don't
  need access to instance data.
'''

class Math:
    def __init__(self, num):
        self.num = num

    def addToNum(self, n):
        self.num = self.num + n

    @staticmethod
    def add(a, b):
        return a + b
    

# result = Math.add(1, 2)
# print(result)


a = Math(5)
print(a.num)
a.addToNum(6)
print(a.num)