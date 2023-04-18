# hierarchical Inheritance
class ParentClass:
    def method1(self): # base class
        print("This method1 is in Parent Class")
        
    
        
class ChildClass1(ParentClass): # derived/child class1
    def method2(self): 
        print("This method2 is in ChildClass1")
        
class ChildClass2(ParentClass): # derived/child class2
    def method3(self):
        print("This method3 is in ChildClass2")
        
        
ch1 = ChildClass1()
ch2 = ChildClass2()
ch1.method1()
ch2.method1()

#===================== 
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
        
        
class BBAStudent(Student):
    def party(self):
        print("All day party")
        
#==================
s1 = CSEStudent("Bob", 11, 3)
s2 = BBAStudent("Carol", 35)
s1.details()
s2.details()
s1.cry()
s2.party()