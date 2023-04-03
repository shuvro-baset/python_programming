# todo: operator Overloading

'''
    using python default method in a class we can overload it.
    And it's called operator overloading
'''


class Data:
    def __init__(self, x):
        self.x = x

    # adding two objects using default method then overload it.
    def __add__(self, other):
        return self.x + other.x


num1 = Data(1)
num2 = Data(23)
str1 = Data("CSE")
str2 = Data("222")

print(num1 + num2)  # num1.__add__(num2)
print(str1 + str2)


