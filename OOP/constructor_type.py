# Non parameterized Constructor
class Employee1:
    pass


emp1 = Employee1()


class Employee2:
    def __int__(self):
        print("similar thing as Non-parameterized Constructor")


emp2 = Employee2()


# Parameterized Constructor
class Employee3:
    def __int__(self, name):
        self.name = name
        print("parameterized Constructor")


emp2 = Employee3()
