from collections.abc import Iterable
from abc import ABC, abstractmethod

""" 1. Creating a simple class in Python """


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} says hello!"


dog = Animal("Charlie")
print(dog.speak())

""" 2. Creating a subclass (Inheritance) """


class Dog(Animal):
    def speak(self):
        return f"{self.name} barks!"


dog = Dog("Charlie")
print(dog.speak())

""" 3. Using the super() function """


class Animal2:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} says hello!"


class Dog2(Animal2):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed


dog2 = Dog2("Charlie", "Bulldog")
print(dog2.breed)

""" 4. Creating a property """


class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value >= 0:
            self._radius = value
        else:
            raise ValueError("Radius must be positive")


circle = Circle(5)
print(circle.radius)
circle.radius = 10
print(circle.radius)

""" 5. Encapsulation – Private members """


class MyClass:
    def __init__(self):
        self.public = "Public"
        self._protected = "Protected"
        self.__private = "Private"


obj = MyClass()
print(obj.public)
print(obj._protected)
# print(obj.__private)  # This will raise an AttributeError


""" 6. Polymorphism – Using Inbuilt Abstract Base Classes (ABC) """


def get_length(item):
    if isinstance(item, Iterable):
        return len(item)
    else:
        return "Not iterable"


print(get_length("Hello"))
print(get_length([1, 2, 3]))
print(get_length(123))

""" 7. Defining an Abstract Base Class(ABC) """


class AbstractAnimal(ABC):
    @abstractmethod
    def speak(self):
        pass


class Dog(AbstractAnimal):
    def speak(self):
        return "Boww Boww!"


# You can't instantiate an AbstractAnimal
# animal = AbstractAnimal()  # This will raise a TypeError

dog = Dog()
print(dog.speak())

""" 8. Using class methods and static methods """


class MyClass:
    @classmethod
    def class_method(cls):
        return "Class method called"

    @staticmethod
    def static_method():
        return "Static method called"


print(MyClass.class_method())
print(MyClass.static_method())

""" 9. Operator Overloading in Python """


class Mango:
    def __init__(self, x):
        self.x = str(x)

    def __add__(self, y):
        return self.x + y.x


obj1 = Mango(7)
obj2 = Mango('mangoes')
print(obj1 + obj2)

""" 10. Using Special methods for string representations (repr and str) """


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old."

    def __repr__(self):
        return f"Person('{self.name}', {self.age})"


p = Person("Bob", 30)
print(str(p))
print(repr(p))

""" 11. Using composition in Python OOP """


class Salary:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


s = Salary(15000, 5000)
e = Employee("Ashwin", s)
print(e.salary.pay)

""" 12. Using multiple inheritance """


class Parent1:
    def method1(self):
        return "Parent1's method called"


class Parent2:
    def method2(self):
        return "Parent2's method called"


class Child(Parent1, Parent2):
    pass


c = Child()
print(c.method1())
print(c.method2())

""" 
    13. Creating a Singleton class in Python
    A singleton class allows the creation of only one instance of itself. 
"""


class Singleton:
    _instance = None

    @staticmethod
    def getInstance():
        if Singleton._instance is None:
            Singleton()
        return Singleton._instance

    def __init__(self):
        if Singleton._instance is not None:
            raise Exception("This class is a singleton!")
        else:
            Singleton._instance = self


s = Singleton.getInstance()
print(s)

""" 
    15. Using Mixin classes in Python
    A mixin class provides methods to other classes, but it is not considered a parent class itself.
 
"""


class Mixin1(object):
    def test(self):
        print("Mixin1")


class Mixin2(object):
    def test(self):
        print("Mixin2")


class MyClass(Mixin1, Mixin2):
    pass


obj = MyClass()
obj.test()
