# todo: Encapsulation
'''
    when we need to restrict any data or function access outside of the class then we should make that variable and function encapsulated
'''


class Student:
    def __int__(self, name, id):
        self.name = name
        self.__id = id  # private variable

    def details(self):
        print("Name:", self.name, "ID: ", self.__id)

    def update_id(self, id):  # update method for update id
        if (id > 0):
            self.__id = id
        else:
            print("Invalid id, enter id again")


# =================
s1 = Student("Bob", 11)
s2 = Student("Carol", 32)

s1.details()
s2.details()

#################################
# todo: getter & setter method
'''
    method naming convention for encapsulating data and function to get and set variable
'''


class Student2:
    def __int__(self, name, id):
        self.name = name
        self.__id = id  # private variable

    def details(self):
        print("Name:", self.name, "ID: ", self.__id)

    def set_id(self, id):  # update method for update id
        if (id > 0):
            self.__id = id
        else:
            print("Invalid id, enter id again")

    def get_id(self):
        return self.__id

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name


# ==================
s1 = Student2("Bob", 11)
s2 = Student2("Carol", 32)
s2.set_id(44)
s1.details()
s2.details()

# todo: method encapsulation
'''
    - doing same thing as variable
    - using double underscore before method name and call this method under any class method
        we don't want to give access this method outside of the class
'''
