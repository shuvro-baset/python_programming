# hybrid Inheritance
class ParentClass:
    def method1(self): # base class
        print("This method1 is in ParentClass")
        
        
class ChildClass1(ParentClass): # derived/child class1
    def method2(self):
        print("This method2 is in ChildClass1")

class ChildClass2(ChildClass1): # derived/child class2
    def method3(self):
        print("This method3 is in ChildClass2")
        
class ChildClass3(ChildClass1): # derived/child class3
    def method4(self):
        print("This method4 is in ChildClass3")
        
ch1 = ChildClass3()
ch1.method1()
ch1.method2()