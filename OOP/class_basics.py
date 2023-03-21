# Non parameterized Constructor
class Employee1:
    pass


emp1 = Employee1()


class Employee2:
    def __int__(self):
        print("similar thing as Non-parameterized Constructor")


emp2 = Employee2()


# Parameterized Constructor
class Employee3:
    def __int__(self, name):
        self.name = name
        print("parameterized Constructor")


emp2 = Employee3()

"""
    Class Object Constructor attributes
"""


class Student:
    def __int__(self, name, id):
        self.name = name  # instance variable
        self.id = id  # instance variable
        print("a student object created")

    def details(self):  # instance method
        print("Name:", self.name, "Id:", self.id)


# variable = class_name()
s1 = Student("Baset", 23)  # creating object with passing objects attributes
s1.details()  # calling instance method
