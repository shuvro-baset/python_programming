# todo: Inheritance
'''
    A software modelling approach of OOP enables extending of an existing class to build a new class, 
    instead of building from scratch. In OOP terminology, this characteristic is called inheritance,
    the existing class is called base or parent class, while the new class is called child or sub class.

    * paren class is the being inherited from, also called base class
    * child class is the class that inherits from another class, also called derived class.

    Inheritance comes into picture when a new class possesses that 'Is a' relationship with an existing class.

    # Benefits of inheritance
        - code reusability, readability, and scalability
        - reduction of code repetition
        - placement of all the standard methods and attributes in the parent class ensures accessibility by the child class derived from it.
        - Division of the code into multiple classes, makes the applications look better, and the error identification is easy.
        - well representation of real-world relationships
        - transitive in nature, which means that if class B inherits from another class A, then all the subclasses of B would automatically inherit from class A.

    # types of inheritance
        - single inheritance
            - in which there is one base class and one derived class
        - multiple inheritance
            - A class can be derived from more then one base classes
        - multilevel inheritance
            - we can inherit a derived class from another derived class
        - hybrid inheritance
            - hybrid inheritance involves multiple inheritance taking place
        - hierarchical inheritance
            - In which there is single base class and multiple derived class
'''


# The code below shows how a class can inherit from another class.
# We have two classes, `Date` and `Time`. Here `Time` inherits from
# `Date`.

# Any class inheriting from another class (also called a Parent class)
# inherits the methods and attributes from the Parent class.

# Hence, any instances created from the class `Time` can access
# the methods defined in the parent class `Date`.


class Date(object):
    def get_date(self):
        print("2016-05-14")


class Time(Date):
    def get_time(self):
        print("07:00:00")


# Creating an instance from `Date`
dt = Date()
dt.get_date()  # Accesing the `get_date()` method of `Date`
print("--------")

# Creating an instance from `Time`.
tm = Time()
tm.get_time()  # Accessing the `get_time()` method from `Time`.
# Accessing the `get_date() which is defined in the parent class `Date`.
tm.get_date()


# inheritance-2.py

# The code below shows another example of inheritance
# Dog and Cat are two classes which inherits from Animal.
# This an instance created from Dog or Cat can access the methods
# in the Animal class, ie.. eat().

# The instance of 'Dog' can access the methods of the Dog class
# and it's parent class 'Animal'.

# The instance of 'Cat' can access the methods of the Cat class
# and it's parent class 'Animal'.

# But the instance created from 'Cat' cannot access the attributes
# within the 'Dog' class, and vice versa.


class Animal(object):
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print("%s is eating/drinking %s" % (self.name, food))


class Dog(Animal):
    def fetch(self, thing):
        print("%s goes after the %s" % (self.name, thing))


class Cat(Animal):
    def swatstring(self):
        print("%s shred the string!" % self.name)


dog = Dog("Tuffy")
cat = Cat("Mona")

dog.fetch("paper")
dog.eat("bone")
print("--------")
cat.eat("milk")
cat.swatstring()

'''
O/P-
Tuffy goes after the paper
Tuffy is eating/drinking bone
--------
Mona is eating/drinking milk
Mona shred the string!
'''

# The below methods would fail, since the instances doesn't have
# have access to the other class.

cat.fetch("frizbee")
dog.swatstring()


# inheriting-init-constructor-1.py

# This is a normal inheritance example from which we build
# the next example. Make sure to read and understand the


class Animal(object):
    def __init__(self, name, thing):
        self.name = name
        self.thing = thing


class Dog(Animal):
    def fetch(self):
        print("%s goes after the %s" % (self.name, self.thing))


dog = Dog("Tuffy", "Ball")
print("The dog's name is %s and he plays %s" % (dog.name, dog.thing))
dog.fetch()
'''
O/P-
The dog's name is Tuffy and he plays Ball
Tuffy goes after the Ball
'''


# ANOTHER WAY TO ACCESS
class Animal(object):
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    def fetch(self, thing):
        print("%s goes after the %s" % (self.name, thing))


d = Dog("TUFFY")
print("The dog's name is", d.name)
d.fetch("Ball")
'''
O/P-
The dog's name is TUFFY
TUFFY goes after the Ball
'''


# multiple-inheritance-1.py

# Python supports multiple inheritance and uses a depth-first order
# when searching for methods.
# This search pattern is call MRO (Method Resolution Order)

# This is the first example, which shows the lookup of a common
# function named 'dothis()', which we'll continue in other examples.

# As per the MRO output, it starts in class D, then B, A, and lastly C.

# Both A and C contains 'dothis()'. Let's trace how the lookup happens.

# As per the MRO output, it starts in class D, then B, A, and lastly C.

# class `A` defines 'dothis()' and the search ends there. It doesn't go to C.

# The MRO will show the full resolution path even if the full path is
# not traversed.

# The method lookup flow in this case is : D -> B -> A -> C


class A(object):
    def dothis(self):
        print("doing this in A")


class B(A):
    pass


class C(object):
    def dothis(self):
        print("doing this in C")


class D(B, C):
    pass


d_instance = D()
d_instance.dothis()  # <== This should print from class A.

print("\nPrint the Method Resolution Order")
print(D.mro())

'''
O/P-
doing this in A

Print the Method Resolution Order
[<class '__main__.D'>, <class '__main__.B'>, <class '__main__.A'>, <class '__main__.C'>, <class 'object'>] 
'''

# multiple-inheritance-2.py

# Python supports multiple inheritance

# It uses a depth-first order when searching for methods.
# This search pattern is call MRO (Method Resolution Order)

# This is a second example, which shows the lookup of 'dothis()'.
# Both A and C contains 'dothis()'. Let's trace how the lookup happens.

# As per the MRO output using depth-first search,
# it starts in class D, then B, A, and lastly C.

# Here we're looking for 'dothis()' which is defined in class `C`.
# The lookup goes from D -> B -> A -> C.

# Since class `A` doesn't have `dothis()`, the lookup goes back to class `C`
# and finds it there.


class A(object):
    def dothat(self):
        print("Doing this in A")


class B(A):
    pass


class C(object):
    def dothis(self):
        print("\nDoing this in C")


class D(B, C):
    """Multiple Inheritance,
    D inheriting from both B and C"""

    pass


d_instance = D()

d_instance.dothis()

print("\nPrint the Method Resolution Order")
print(D.mro())

'''
O/P-
Doing this in C

Print the Method Resolution Order
[<class '__main__.D'>, <class '__main__.B'>, <class '__main__.A'>, <class '__main__.C'>, <class 'object'>] 
'''


# multiple-inheritance-3.py

# Python supports multiple inheritance
# and uses a depth-first order when searching for methods.
# This search pattern is call MRO (Method Resolution Order)

# Example for "Diamond Shape" inheritance
# Lookup can get complicated when multiple classes inherit
# from multiple parent classes.

# In order to avoid ambiguity while doing a lookup for a method
# in various classes, from Python 2.3, the MRO lookup order has an
# additional feature.

# It still does a depth-first lookup, but if the occurrence of a class
# happens multiple times in the MRO path, it removes the initial occurrence
# and keeps the latter.

# In the example below, class `D` inherits from `B` and `C`.
# And both `B` and `C` inherits from `A`.
# Both `A` and `C` has the method `dothis()`.

# We instantiate `D` and requests the 'dothis()' method.
# By default, the lookup should go D -> B -> A -> C -> A.
# But from Python 2.3, in order to reduce the lookup time,
# the MRO skips the classes which occur multiple times in the path.

# Hence the lookup will be D -> B -> C -> A.


class A(object):
    def dothis(self):
        print("doing this in A")


class B(A):
    pass


class C(A):
    def dothis(self):
        print("doing this in C")


class D(B, C):
    pass


d_instance = D()
d_instance.dothis()

print("\nPrint the Method Resolution Order")
print(D.mro())

'''
O/P-
doing this in C

Print the Method Resolution Order
[<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>] 
'''