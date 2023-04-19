class Engine:
    def __init__(self, cc):
        self.capacity = cc
        
    def start(self):
        print("Engine started")
        
    def stop(self):
        print("Engine stopped")
        
class Car:
    def __init__(self, name, cc):
        self.name = name 
        self.engine = Engine(cc) # creating engine object as a Has-A relationship
        
    def run(self):
        self.engine.start()
        print("Car is running")
        
c1 = Car("BMW", 2000)
c1.run()