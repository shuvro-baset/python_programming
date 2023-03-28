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

    def product(self, *nums):
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
