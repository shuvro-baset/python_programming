class Product:
    quantity = 200

    # constructor method. it initializes the class. this method is being called automatically for every object creation time
    def __init__(self, name, price):
        self.name = name
        self.price = price

    # this is instance method. this method will call with reference of an object
    def summer_discount(self, discount_percent):
        self.price = self.price - self.price*discount_percent/100

# # creating an object of Product
# p1 = Product()
# # printing p1 and it will return the memory address of this object
# print(p1)
#
# # accessing the class attributes
# print(p1.quantity)