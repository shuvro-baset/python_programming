[Object-Oriented Programming in Python](https://salt-akubra-1de.notion.site/Object-Oriented-Programming-Python-101406c88f9d8025b750f1911430d39d?pvs=4)


# Object Oriented Programming (Python)

**Object-Oriented Programming (OOP)** in Python focuses on creating reusable and modular code.  The object-oriented paradigm structures programs by using **classes** and **objects**. Objects represent real-world entities such as books, houses, or pencils. The main goal of OOP is to design programs that emphasize **reusability**, allowing code to be more organized and scalable. By creating objects, OOP provides a systematic approach to problem-solving and makes complex software easier to maintain and extend.

---

- Blog Resources
    - [x]  [https://realpython.com/python3-object-oriented-programming/](https://realpython.com/python3-object-oriented-programming/)
    - [ ]  https://github.com/Shikha-code36/Object-Oriented-Programming-OOPs-Python
    - [ ]  https://github.com/arvimal/oop_with_python
    - [x]  https://www.freecodecamp.org/news/object-oriented-programming-in-python/
    - [ ]  https://github.com/ariannedee/oop-python

---

- **Class**
    - It is you can say a template. Classes are the building blocks in Object Oriented Programming. Classes can be seen as blueprints from which you create your Instances or Objects. In Python, classes are defined by the “Class” keyword
    
    ```python
    class myClass():
    	pass
    ```
    
    - A class is a collection of instance variables and related methods that define a particular object type. You can think of a class as an object blueprint or template.
    - Attributes are the names given to the variables that make up a class
    - A class instance with a defined set of properties is called an object. As a result, the same class can be used to construct as many objects as needed.
    - Classes are the building blocks of OOP.
    - Classes can be seen as blueprints from which you create your instances.
    - Class Components
        - Data ( the attributes)
        - Behavior (the method)
- **Class Attribute**
    
    ```python
    # Here we define an attribute under the class `YourClass`
    # as well as an attribute within the function.
    
    # The attribute defined in the class is called `class attributes`
    # and the attribute defined in the function is called `instance attributes`.
    
    class YourClass(object):
        classy = 10
    
        def set_val(self):
            self.insty = 100
    
    dd = YourClass()
    dd.classy   # This will fetch the class attribute 10.
    dd.set_val()
    dd.insty #100  # This will fetch the instance attribute 100.
    
    # Once `dd` is instantiated, we can access both the class and instance
    # attributes, ie.. dd.classy and dd.insty.
    
    # --------------------------------------------------------
    # The code below shows two important points:
    
    # a) A class attribute can be overridden in an instance, even
    # though it is bad due to breaking Encapsulation.
    
    # b) There is a lookup path for attributes in Python. The first being
    # the method defined within the class, and then the class above it.
    
    # We are overriding the 'classy' class attribute in the instance 'dd'.
    # When it's overridden, the python interpreter reads the overridden value.
    # But once the new value is deleted with 'del', the overridden value is no longer
    # present in the instance, and hence the lookup goes a level above and gets it from
    # the class.
    
    class YourClass(object):
        classy = "class value"
    
    dd = YourClass()
    print(dd.classy)  # < This should return the string "class value"
    
    dd.classy = "Instance value"
    print(dd.classy)  # This should return the string "Instance value"
    
    # This will delete the value set for 'dd.classy' in the instance.
    del dd.classy
    # Since the overriding attribute was deleted, this will print 'class value'.
    print(dd.classy)
    
    # --------------------------------------------------------
    # This code shows that an Instance can access it's own
    # attributes as well as Class attributes.
    
    # We have a class attribute named 'count', and we add 1 to
    # it each time we create an instance. This can help count the
    # number of instances at the time of instantiation.
    
    class InstanceCounter(object):
        count = 0
    
        def __init__(self, val):
            self.val = val
            InstanceCounter.count += 1
    
        def set_val(self, newval):
            self.val = newval
    
        def get_val(self):
            print(self.val)
    
        def get_count(self):
            print(InstanceCounter.count)
    
    a = InstanceCounter(5)
    b = InstanceCounter(10)
    c = InstanceCounter(15)
    
    for obj in (a, b, c):
        print("value of obj: %s" % obj.get_val())
        print("Count : %s" % obj.get_count())
    ```
    
- **Methods-Functions**
    - Inside classes, you can define functions or methods that are part of this class
    - Difference between functions and methods
        - Functions can be called only by their name, as they are defined independently. But methods can't be called by its name only, we need to invoke the class by a reference of that class in which it is defined, i.e. method is defined within a class and hence they are dependent on that class.
    
    ```python
    def method1 (self):
    print("OOPs")
    def method2 (self,someString):
    print ("Program-Method"+ someString)
    
    class myClass():
        def method1 (self):
            print("OOPs")
        def method2 (self,someString): 
            print ("Program-Method" + someString)
    ```
    
- **Constructor**
    - Constructors are generally used for instantiating an object. The task of constructors is to initialize(assign values) to the data members of the class when an object of the class is created. In Python the **init**() method is called the constructor and is always called when an object is created.
    - A constructor is used to create an instance of a class.
    - The constructor (`__init__()`) is automatically called when a new object is created using the class. If multiple objects are made, the constructor will be called each time.
    - All instance variables are initialized within the constructor.
    - Every class has a constructor, whether explicitly defined or not. If not defined, Python provides a default constructor.
    - There are two types of constructors:
        - **Non-parameterized (default) constructor**:
            
            ```python
            def __init__(self):
                pass
            ```
            
        - **Parameterized constructor**: Accepts parameters to initialize instance variables.
            
            ```python
            def __init__(self, name):
                [self.name](http://self.name) = name
            ```
            
    - The constructor always accepts `self` as its first argument, which allows the class to access its attributes and methods.
- **Self**
    - Self means itself as an object for the class.
    - creating an object and assigning it to a variable then will create a memory location in a memory that was passed in the self keyword for that object.
    - Two objects’ memory location or address can't be the same.
    - We can’t access the object instance variable without referring object.
    - We should refer to ourselves when creating any function under the class.
    - when we call a function that was derived under the class then the self automatically passed
    - `__dict__()` calling this method with or by referring self keyword returns all the properties and values as a dictionary.
- **Magic Method**
    
    ```python
    # In the backend, python is mostly objects and method
    # calls on objects.
    
    # Here we see an example, where the `print()` function
    # is just a call to the magic method `__repr__()`.
    
    class PrintList(object):
        def __init__(self, my_list):
            self.mylist = my_list
    
        def __repr__(self):
            return str(self.mylist)
    
    printlist = PrintList(["a", "b", "c"])
    print(printlist.__repr__()) #['a', 'b', 'c']
    
    # To read more on magic methods, refer :
    # http://www.rafekettler.com/magicmethods.html
    
    my_list_1 = ["a", "b", "c"]
    
    my_list_2 = ["d", "e", "f"]
    
    print("\nCalling the `+` builtin with both lists")
    print(my_list_1 + my_list_2)
    
    print("\nCalling `__add__()` with both lists")
    print(my_list_1.__add__(my_list_2))
    '''
    O/P-
    Calling the `+` builtin with both lists
    ['a', 'b', 'c', 'd', 'e', 'f']
    
    Calling `__add__()` with both lists
    ['a', 'b', 'c', 'd', 'e', 'f']
    '''
    ```
    
- **Objects**
    - How to make an object of the class?
        - `obj = myClass()`
    - How to call a method in a class?
        - obj.method1()
        obj.method2("Learning OOPs")
    - Notice that when we call the method1 or method2, we don’t have to supply the self-keyword. That’s automatically handled for us by the Python runtime.
    - Python runtime will pass a “self” value when you call an instance method on an instance, whether you provide it deliberately or not
    - Just work on non-self-arguments
- **Class or Static Variable**
    - It’s not a variable of any objects. It is a variable of the class
    - it's not dependent on the object
    - It is a property of that class
    - we can access or refer to this variable by the class name
- **Type of  Method**
    - 3 types of methods used in Python
        
        ```python
        class MyClass:
            def method(self):
                return 'instance method called', self
        
            @classmethod
            def classmethod(cls):
                return 'class method called', cls
        
            @staticmethod
            def staticmethod():
                return 'static method called'
                
        
        Instance Methods-
        The first method on MyClass, called method, is a regular instance method.
        the method takes one parameter, self, which points to an instance of MyClass when the method is called 
        (but of course instance methods can accept more than just one parameter).
        
        It can modify object's state and class state.
        Through the self parameter, instance methods can freely access attributes and other methods on the same object. 
        Not only can they modify object state, instance methods can also access the class itself through the self.__class__ attribute. This means instance methods can also modify class state.
        '''
        '''
        >>> obj = MyClass()
        >>> obj.method()
        ('instance method called', <MyClass instance at 0x10205d190>)
        This confirmed that method (the instance method) has access to the object instance (printed as <MyClass instance>) via the self argument.
        
        When the method is called, Python replaces the self argument with the instance object, obj.
        
        we can also do like this 
        >>> MyClass.method(obj)
        ('instance method called', <MyClass instance at 0x10205d190>)
        '''
        
        '''
        Class Methods-
        @classmethod decorator to flag it as a class method.
        
        Instead of accepting a self parameter, class methods take a cls parameter that points to the class—and not the object instance—when the method is called.
        Because the class method only has access to this cls argument, it can’t modify object instance state. 
        That would require access to self. 
        However, class methods can still modify class state that applies across all instances of the class.
        '''
        '''
        >>> obj.classmethod()
        ('class method called', <class MyClass at 0x101a2f4c8>)
        Calling classmethod() showed us it doesn’t have access to the <MyClass instance> object, but only to the <class MyClass> object, representing the class itself (everything in Python is an object, even classes themselves).
        '''
        
        '''
        Static Methods-
         @staticmethod decorator to flag it as a static method.
        
        This type of method takes neither a self nor a cls parameter (but of course it’s free to accept an arbitrary number of other parameters).
        
        Therefore a static method can neither modify object state nor class state.
        Static methods are restricted in what data they can access - and they’re primarily a way to namespace your methods.
        '''
        '''
        >>> obj.staticmethod()
        'static method called'
        '''
        ```
        
    
- **Encapsulation**
    - Encapsulation means restricting the user from accessing some important attributes or methods outside the class.
    - Public, private, protected variable
    - Private variables or methods can't be accessible outside of the class.
    - getter and setter method
        - these two decorator is used for method encapsulation
        - getter is default method. Just use @property decorator and it allows you to get objects attribute.
        - with the function name, you can call the setter method so that you can reassign the objects attribute.
- **Access Modifier**
    - Public, Private, and Protected are called access modifiers.
- **Inheritance**
    - parent class/superclass/ base class
    - under the parent class, there will be a class called subclass / derived class/child class
    - inheritance is a relationship. The child will get the parent's property.
    - Single Inheritance, multiple, multilevel, hybrid, hierarchical inheritance.
- **Super**
    - with inheritance, the super() function is used.
    - It allows us to call a method of the parent class.
- MRO
    - Method Resolution Order
    - this will be used when function overriding is used.  The same class will defined in a multiple class. Based on the reference 1st method will be called.
- **`__str__()` Method**
    - By default if any object is called the `__str__()` method. It returns the memory location
        - 
        
        ```python
        s1 = S()
        print(s1) #return memory location
        print(s1.__str__()) # return memory location
        ```
        
    - If we want to return something rather than the memory location from this method, we must override it under the class. It should return a string.
    - It is also called a string representation.
- **Polymorphism**
    - ‘Polymorphism’ comes from the Greek language and means ‘something takes on multiple forms’.
    - same function different implementation.
    - 2 types of polymorphism.
        - Method Overloading. Python does not support it. we make it.
        - Method Overriding.
    - Method Overloading
        - Under the class, if a method writes multiple times with different params then it is called method overloading. But Python does not support it.
        - To achieve this we can use (*) arbitrary params in the function.
            
            ```python
            def methodOverloading(self, *nums):
            	sum = 0
            	for x in nums:
            		sum = sum + x
            	return sum
            ```
            
        - Another way to achieve this using a dispatch decorator.
- **Abstraction**
    - Abstraction in Python is a core principle of Object-Oriented Programming (OOP) that simplifies complex systems by hiding unnecessary details and exposing only the essential features. It helps in reducing complexity, improving code readability, and making maintenance easier by focusing on what an object does rather than how it does it.
    - Abstraction hides the internal implementation details and exposes only the necessary attributes or methods to interact with the object.
    - don't create any object from the abstraction class
    - abstract method will declare only no implementation.
    - in a sub-class, we need to override the abstract class methods. otherwise it will not work.