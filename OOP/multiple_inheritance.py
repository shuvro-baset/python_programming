# multiple Inheritance
class ParentClass1:
    def method1(self): # base class
        print("This method1 is in ParentClass1")
        
    
        
class ParentClass2: # base class2
    def method2(self): 
        print("This method2 is in ParentClass2")
        
class ChildClass(ParentClass1, ParentClass2): # derived/child class
    def method3(self):
        print("This method3 is in ChildClass")
        
        
ch1 = ChildClass()
ch1.method1()
ch1.method1()
ch1.method1()
