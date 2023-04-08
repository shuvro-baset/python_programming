class Book:
    def __int__(self, name, author):
        self.name = name
        self.author = author
        self.price = 0

    def set_price(self, price):
        self.price = price

    def get_price(self):
        return self.price

    def details(self):
        print("Book Name:", self.name,
              "\nAuthor: ", self.author,
              "\nPrice: ", self.price, "Taka")


# ============================================
b1 = Book("Ami Topu", "Jafor Iqbal")
b1.details()
b1.set_price(55)
b1.details()
