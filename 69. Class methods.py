# Class methods in python

class Employee:
    company = "Apple"

    def show(self):
        print(f"The name is {self.name} and company is {self.company}")

    # def changeCompany(cls, newCompany):
    #     cls.company = newCompany

    @classmethod 
    def changeCompany(cls, newCompany):
        cls.company = newCompany


e1 = Employee()
e1.name = "harry"
e1.show()
e1.changeCompany("Tesla")
e1.show()
print(Employee.company) #without class method it will give "Apple", 

e2 = Employee()
e2.name = "Rohan"
e2.show()


# with @classmethod decorator, it will change the method.