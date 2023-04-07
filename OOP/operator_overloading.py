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


###############################
class House:
    def __int__(self, w, d):
        self.window = w
        self.door = d

    def view(self):
        print("The house hase", self.window, "window(s) and", self.door, "door(s)")

    def __add__(self, other):
        new_window = self.window + other.window
        new_door = self.door + other.door
        obj = House(new_window, new_door)  # create new House object
        return obj
        # return "new house hase" + str(new_window) + "windows and" + str(new_door) + "doors"


h1 = House(3, 6)
h2 = House(5, 2)
h1.view()
h2.view()
h3 = h1 + h2
h3.view()
# print(h1 + h2)
