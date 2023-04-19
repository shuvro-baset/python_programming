'''
    TODO: Abstract class
    
    * Can be considered as a blueprint for other classes
    * Defines a common interface for a set of subclasses
    * Provides common attributes and methods for all subclasses for reduction of code duplication
    * contains one or more abstract methods
    * an abstract method has a declaration but does not have an implementation
    * we use abstract class when we design large functional units

    TODO: Abstract Base Class
    * Python does not provide abstract classes by default
    * Comes with a module that provides the base for defining Abstract Base classes which is ABC
    * A method becomes abstract when decorated with the keyword @abstractmethod
        from abs import ABC, abstractmethod
'''

from abc import ABC, abstractmethod
class Food(ABC): # making abstract class
    @abstractmethod
    def taste(self): # making abstract method
        pass
    
class Pizza(Food):
    def taste(self): # overriding abstract method
        print("Pizza is delicious")
        
    def size(self):
        print("12-inch pizza")
        
p = Pizza()
p.taste()
p.size()