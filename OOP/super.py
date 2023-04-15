# todo: super()
'''
    super(): with inheritance, the super() function in python actually comes in quite handy. it allows us to call a method of the parent class
'''


class ParentClass:
    def feature1(self):
        print("feature1 is from ParentClass")
        
    def feature2(self):
        print("feature2 is from ParentClass")
        
        
class ChildClass(ParentClass):
    def feature3(self):
        super().feature1()
        print("feature3 is from ChildClass")
        super().feature2()
        
obj = ChildClass()
obj.feature3()