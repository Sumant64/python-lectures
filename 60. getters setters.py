# Getters and setters in python

class MyClass:
    def __init__(self, value):
        self._value = value

    def show(self):
        print(f"Value is {self._value}")

    @property
    def value(self):
        return f"The value is {self._value}"

    @property
    def ten_value(self):
        return 10 * self._value
    
    @ten_value.setter
    def ten_value(self, new_value):
        self._value =  new_value / 10

obj = MyClass(20)
obj.show()

print(obj.value)
print(obj.ten_value)

# setting value
obj.ten_value = 30
obj.show()
