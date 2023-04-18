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

#=====================================
class A:
    def __init__(self):
        print("__init__ of class A")
    
    def method1(self):
        print("Method1 of class A")

class B:
    def __init__(self):
        print("__init__ of class B")
        
    def method1(self):
        print("Method1 of class B")
        
class C(A, B):
    def __init__(self):
        # super().__init__() # this super will call class A __init__() as for method resolution order
        # B.__init__(self)  # this time by force called class B __init__() 
        print("__init__ of class C")
        
    def method2(self):
        print("Method2 of class C")
    
#====================
c1 = C()
c1.method1()
B.method1(c1) # calling class B method by force and passing c1 object