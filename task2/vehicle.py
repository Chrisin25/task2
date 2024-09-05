from abc import ABC,abstractmethod


class Vehicle(ABC):
    def __init__(self,vehicle_type):
        if type(vehicle_type)!= str:
            print("invalid vehicle type")
        else:
            self.vehicle_type=vehicle_type
    @abstractmethod
    def get_fuel_efficiency(self):
        pass
    def describe(self):
        print("vehicle type:",self.vehicle_type)
    @classmethod
    def from_name(cls,vehicle_type):
        if type(vehicle_type)!= str:
            print("invalid vehicle type")
        elif vehicle_type=="car":
            return Car()
        elif vehicle_type=="truck":
            return Truck()
        else:
            return "unknown vehicle type"

class Car(Vehicle):
    def __init__(self):
        super().__init__("Car")
    def get_fuel_efficiency(self):
        return "25 miles per gallon"

class Truck(Vehicle):
    def __init__(self):
        super().__init__("Truck")
    def get_fuel_efficiency(self):
        return "15 miles per gallon"

car1=Car()
car1.describe()
print("fuel efficiency of car:",car1.get_fuel_efficiency())

truck1=Truck()
truck1.describe()
print("fuel efficiency of truck:",truck1.get_fuel_efficiency())

vehicle_type=input("enter vehicle type:car,truck")
vehicle1=Vehicle.from_name(vehicle_type)
vehicle1.describe()
print("fuel efficiency of ",vehicle_type,": ",vehicle1.get_fuel_efficiency())




