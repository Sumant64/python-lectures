# Typecasting in python

'''
Typecasting in python
---------------------
o The conversion of one data type into the other data type is known as
  type casting in python or type convertion in python.

o Python supports a wide variety of functions or methods like:
  int(), float(), str(), ord(), hex(), oct(), tuple(), list(),
  set(), dict(), etc.
'''

a = "1"
b = "2"
print(a + b)
print(int(a) + int(b))

# ====================================
# Implicity type casting
# automatically convert one data type to other

c = 1.9
d = 8

print(c + d)
print(type(c + d)) #converts automatically to float
