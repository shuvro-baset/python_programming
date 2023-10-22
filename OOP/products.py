class Product:
    quantity = 200

    # constructor method. it initializes the class. this method is being called automatically for every object creation time
    def __init__(self, name, price):
        self.name = name
        self.price = price

# # creating an object of Product
# p1 = Product()
# # printing p1 and it will return the memory address of this object
# print(p1)
#
# # accessing the class attributes
# print(p1.quantity)