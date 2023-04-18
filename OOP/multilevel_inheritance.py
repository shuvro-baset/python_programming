# Multilevel Inheritance
class ParentClass:
    def method1(self): # base class
        print("This method1 is in Parent Class")
        
    
        
class ChildClass1(ParentClass): # derived/child class1
    def method2(self): 
        print("This method2 is in ChildClass1")
        
class ChildClass2(ChildClass1): # derived/child class2
    def method3(self):
        print("This method3 is in ChildClass2")
        
ch1 = ChildClass2()
ch1.method1()
ch1.method2()
ch1.method3()

# ===============================
class Student:
    def __init__(self, name, Id):
        self.name = name 
        self.Id = Id
        
    def details(self):
        print("Name: ", self.name, "Id: ", self.Id)

class CSEStudent(Student):
    def __init__(self, name, Id, labs):
        super().__init__(name, Id)
        self.no_of_labs = labs
        
    def cry(self):
        print("CSE Student is crying because of", self.no_of_labs, "labs")
        
        
class CSEFresher(CSEStudent):
    def enroll_CSE110(self):
        print(self.name, "enrolled in CSE110")
        
#====== 
s1 = CSEFresher("Bob", 11, 4)
s2 = CSEFresher("Carol", 12, 4)
s2.details()
s1.details()
s2.enroll_CSE110()