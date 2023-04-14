# todo: method
'''
    - a python method is like a python function
    - it must be called on an object
    - it must put it inside a class
    - a method has a name, and may take parameters and have return statement

    - 3 types of methods in python --
        -- instance method
        -- class method
        -- static method
'''

# todo:instance method
'''
    - instance method are methods which require an object of its class to be created before it can be called
    - instance methods need aclass instance and can access the instance through self.
    - instance method takes more that one parameter, self, which points to an instance of class when the method is called.
    - the self parameter, instance methods can freely access attributes and other methods on the same object
'''

# todo: Class Method
'''
    - A class method is bound to the class and not the object of the class.
        They have the access to the state of the class as it takes a class
        parameter that points to the class and not the object instance
    - Method with a @classmethod decorator to flag it as a class method.
    - Class method don't need a class instance. They can't access the instance(self)
        but they have access to the class itself via cls    
'''


# Example:
class A:
    org_name = "Google"

    def __int__(self, name):
        self.name = name

    @classmethod
    def info(cls):
        return cls.org_name


print(A.info())

# todo: static method
'''
    - Static methods in python are extremely similar to python class level methods.
    - Marked with @staticmethod decorator to flag it as a static method
    - This type of method takes neither a self nor a cls parameter
    - it is free to accept an arbitrary number of other parameters
    - static method can neither modify object state nor class state
    - it can be called without an object for that class, using the class name directly
         if we want to do something extra with a class we can use static methods
    - we generally use static methods to create utility functions
'''


# Example:
class B:
    org_name = "Google"

    def __int__(self, name):
        self.name = name

    @staticmethod
    def detail(cls):
        print("This is a B class")


# B.detail()


class MyClass:
    def method(self):
        print(self, "instance method called ")

    @classmethod
    def class_method(cls):
        print(cls, "class method called")

    @staticmethod
    def static_method():
        print("Static method called")


# todo: example of class variable
class Student:
    uni_name = "UODA U"

    def __int__(self, name, id):
        self.name = name
        self.__id = id

    def details(self):
        print("Name: ", self.name, "ID: ", self.__id, Student.uni_name)

    @classmethod
    def up_uni_name(cls, u_name):
        cls.uni_name = u_name


# ========================
s1 = Student("Bob", 11)
s2 = Student("Caroll", 21)
s1.details()
s2.details()
Student.up_uni_name("Brac University")
s1.details()
s2.details()

# Creating Factory Methods
class Student2:
    uni_name = "Student"
    
    def __init__(self, name, id):
        self.name = name
        self.__id = id
    
    def details(self):
        print("Name: " , self.name, "Id: " , self.__id, Student2.uni_name)
        
    @classmethod
    def up_uni_name(cls, u_name):
        cls.uni_name = u_name
    
    @classmethod
    def from_string(cls, info):
        name, id = info.split('-') 
        obj = cls(name, id)    
        return obj
    
    @staticmethod
    def check_department(id):
        if id[3:5] == "01" : print("CSE")
        elif id[3:5] == "41" : print("CS")
    
          
s1 = Student2("bob", 12)
s2 = Student2.from_string("carol-53")
s1.details()
s2.details()
Student2.check_department("15301007")