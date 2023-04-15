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