# Introduction to oops

'''
Object-Oriented Programming (OOP) in Python is used for several important reasons. 
It helps developers create more organized, reusable, and maintainable code. Here's a 
breakdown of the key reasons we use OOP in Python:

1. Encapsulation:
----------------
o What it is: Encapsulation is the bundling of data (attributes) and methods (functions) that 
  operates on the data into a single unit called a class. It also allows restricting access to some 
  of the object's components (e.g., through private or protected members.)
o Why is matters: It hides the internal state of the object and only exposes a controlled
  interface to the outside world, reducing complexity and potential errors.

2. Inheritance:
--------------
o What it is: Inheritance allows a class (child class) to inherit properties and methods from
  another class (parent class).
o Why it matters: It promotes code reusability and allows you to create more specific classes from
  general ones. You can extend or modify the behavior of existing code wihtout having
  to rewrite it.

3. Polymorphism:
---------------
o What it is: Polymorphism allows objects of different classes to be treated as objects of a 
  common base class. It means that the same method or function can behave differently 
  depending on the type of the object calling it.
o Why it matters: It allows for more flexible and general code. For example,
  you can call a method on different object types, and each will respond
  in its own way, without needing to know the specific type.

4. Abstraction:
--------------
o What it is: Abstraction is the concept of hiding complex implementation
  details and exposing only the essential features of an object. 
o Why it matters: It helps reduce complexity and allows the programmer to focus
  on higher-level functionality. By creating abstract classes or interfaces,
  developes can define a blueprint for future classes without worrying about
  their internal workings.

5. Code Reusability:
-------------------
o OOP makes it easier to reuse code. Once a class is written, it can be reused across
  different parts of the program or even in different programs. 
o By using inheritance, classes can share common functionality, which
  minimizes duplication and makes the codebase easier to maintain.

6. Modularity:
7. Maintainability
8. Real-world Modeling:
  o OOP models real-world entities better than procedural programming.
  For example, you can think of a Car class with attributes like color,
  model, and methods like start_engine(). This makes the code easier to 
  understand, especially for large applications where multiple real-world
  entities interact.

'''

# OOPs Example:

# Class Definitation (Encapsulation)
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self): # Method in the class
        print(f"{self.name} makes a sound")

# Inheritance
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Dog")
        self.breed = breed

    def speak(self): # Polymorphism
        print(f"{self.name} barks")

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, species="Cat")
        self.color = color

    def speak(self): # Polymorphism
        print(f"{self.name} meows")


# Instantiating Objects (Instances of the class)
dog = Dog(name = "Buddy", breed="Golden Retriever")
cat = Cat(name="Whiskers", color="Gray")

# Calling methods (Abstraction)
dog.speak()
cat.speak()