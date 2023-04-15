# Single Inheritance
class ParentClass:
    def method1(self): # base class
        print("This method1 is in Parent Class")
        
    def method2(self): 
        print("This method2 is in Parent Class")
        
class ChildClass(ParentClass): # derived/child class
    def method3(self):
        print("This method3 is in Child Class")
        
ch1 = ChildClass()
ch1.method1()
ch1.method2()
ch1.method3()

##################################### 


class Animal:
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        print(self.name, "is eating")
        
# ==================================== 

class Dog(Animal):
    def bark(self):
        print(self.name, "is barking")
        
a1 = Animal("Jack")
d1 = Dog("Rover")
d1.bark()
d1.eat()

# isinstance(object, classname) , issubclass(class, classname)
print(isinstance(a1, Animal))
print(issubclass(a1, Animal))