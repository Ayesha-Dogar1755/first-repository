class Vehicle:
    def __init__(self, brand, model):
        self.brand=brand
        self.model=model
class Car(Vehicle):
    def __init__(self,brand,model,seats):
        super().__init__(brand,model)
        self.seats=seats
class Bike(Vehicle):
    def __init__(self,brand,model,engine_cc):
        super().__init__(brand,model)
        self.engine_cc=engine_cc
car1=Car("Toyota","Camry",5)
print("Car Brand:",car1.brand)
print("Car Model:",car1.model)
print("Number of Seats:",car1.seats)
bike1=Bike("Yamaha","R15",155)
print("Bike Brand:",bike1.brand)
print("Bike Model:",bike1.model)
print("Engine CC:",bike1.engine_cc)                