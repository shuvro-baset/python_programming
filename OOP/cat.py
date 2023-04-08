class Cat:
    def __int__(self, color, action):
        self.color = color
        self.action = action

    def view(self):
        print(self.color, "cat is", self.action)

    def compare(self, ct):
        if self.action == ct.action:
            print("Both cats are", self.action)
        else:
            print("They are different")


# =============

c1 = Cat("White", "Jumping")
c2 = Cat("Brown", "sitting")

c1.view()
c2.view()

# Todo: pass by reference
c1.compare(c2)  # passing c2 object

# Todo: pass by value
""" 
    when a value is passing 
    list not pass by as value it will be pass as reference    
"""
