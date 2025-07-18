'''
class my_calculator:
    '''
# todo: Method overloading using multiple params
'''

    def product(self, num1, num2=None, num3=None):
        if num1 != None and num2 != None and num3 != None:
            print(num1 * num2 * num3)
        elif num1 != None and num2 != None:
            print(num1 * num2)
        else:
            print(1 * num1)

'''
# todo:  Method Overloading using *
'''

    def product(self, *nums): # here *nums will be tuple
        sum = 1
        for x in nums:
            sum = sum * x
        print(sum)
'''

'''
    use dispatch
    from multipledispatch import dispatch
    note: dispatch decorator received params as data type.
'''
from multipledispatch import dispatch


class MyCalculator:
    @dispatch(int, int)
    def product(self, a, b):
        print(a * b)

    @dispatch(int, int, int)
    def product(self, a, b, c):
        print(a * b * c)

    @dispatch(str, int)
    def product(self, a, b):
        print("If function called with str and int type data then this product will execute")
        print(int(a) * b)


##############
c1 = MyCalculator()
c1.product(4, 5)
c1.product(1, 5, 9)

# Todo: Constructor Overloading
'''
    We can achieve constructor overloading same process as method overloading
'''


class Student:

    def __init__(self, **info):
        if len(info) == 3:
            self.name = info['name']
            self.id = info['id']
            self.CGPA = info['cg']
        elif len(info) == 2:
            self.name = info['name']
            self.id = info['id']
        elif len(info) == 1:
            self.name = info['name']
        print("A student is created")


#############################
s1 = Student(name="Baset", id=75, cg=3.37)
