class Vehicle:
    def __init__(self, brand = "undefined", model_year = 0, milage = 0, price = 0.0):
        self.__brand = brand
        self.__model_year = model_year
        self.__milage = milage
        self.__price = price

    @property
    def brand(self):
        return self.__brand
    @property
    def model_year(self):
        return self.__model_year
    @property
    def milage(self):
        return self.__milage
    @property
    def price(self):
        return self.__price

    @brand.setter
    def brand(self, value):
        self.__brand = value
    @model_year.setter
    def model_year(self, value):
        self.__model_year = value
    @milage.setter
    def milage(self, value):
        self.__milage = value
    @price.setter
    def price(self, value):
        self.__price = value
    def __str__(self):
        return f"Make: {self.brand}  Model: {self.model_year}  Milage: {self.milage}  Price: {self.price}"


class Car(Vehicle):
    def __init__(self, brand, model_year, milage, price, amout_of_doors = 0):
        super().__init__(brand, model_year, milage, price)
        self.__doors = amout_of_doors

    @property
    def doors(self):
        return self.__doors
    @doors.setter
    def doors(self, value):
        self.__doors = value
    def __str__(self):
        return f"Make: {self.brand}  Model: {self.model_year}  Milage: {self.milage}  Price: {self.price}  Doors: {self.doors}"

class Truck(Vehicle):
    def __init__(self, brand, model_year, milage, price, wheel_drive = ''):
        super().__init__(brand, model_year, milage, price)
        self.__wheel_drive = wheel_drive

    @property
    def wheel_drive(self):
        return self.__wheel_drive
    @wheel_drive.setter
    def wheel_drive(self, value):
        self.__wheel_drive = value
    def __str__(self):
        return f"Make: {self.brand}  Model: {self.model_year}  Milage: {self.milage}  Price: {self.price} Drive type: {self.wheel_drive}"
    
class SUV(Vehicle):
    def __init__(self, brand, model_year, milage, price, passenger_capacity = 0):
        super().__init__(brand, model_year, milage, price)
        self.__passenger_capacity = passenger_capacity
    
    @property
    def passenger_capacity(self):
        return self.__passenger_capacity
    @passenger_capacity.setter    
    def passenger_capacity(self, value):
        self.__passenger_capacity = value
    def __str__(self):
        return f"Make: {self.brand}  Model: {self.model_year}  Milage: {self.milage}  Price: {self.price}  Number of passengers: {self.passenger_capacity}"

if __name__ == "__main__":
    truck = Truck("Whatever", 2020, 10000, 2000000, 6)
    truck.brand = "Scania"
    print(truck.brand)
    