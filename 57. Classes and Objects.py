# Classes and Objects

class Person:
    name = "Harry"
    occupation = "Software Developer"
    network = 10

    def info(self):
        print(f"{self.name} is a {self.occupation}")


# a = Person()
# a.name = "Shubham"
# a.occupation = "Accountant"
# print(a.name, a.occupation)
# a.info()

# =================================
# a = Person()
# a.info()

# =================================

a = Person()
b = Person()
a.name = "Shubham"
a.occupation = "Accountant"

b.name = "Nitika"
b.occupation = "HR"
print(a.name, a.occupation)
a.info()
b.info()