# TODO: variable overriding

class Animal:
    def __init__(self, name):
        self.name = name
        self.color = "White"
        
    def eat(self):
        print(self.color, self.name, "is eating")
        
class Dog(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color # variable overriding
        
    def bark(self):
        print(self.color, self.name, "is barking")
        
d1 = Dog("Rover", "Brown")
d1.bark()
d1.eat()


# TODO: method overriding
class A:
    def __init__(self):
        print("__init__ of class A")
    
    def method1(self):
        print("few study")
        
    def method2(self):
        print("you will get all of my properties and methods")
        
class B(A):
    def __init__(self):
        pass
    
    def method1(self): # method overriding
        print("always party")
        super().method1() # method accessing from parent so that both method can execute
        
        
b1 = B()
b1.method1()
b1.method2()