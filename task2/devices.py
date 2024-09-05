from abc import ABC,abstractmethod


class ElectronicDevice(ABC):
    def __init__(self):
        self.brand=input("enter brand:")
        self.model=input("enter model:")
    @abstractmethod
    def power_usage(self):
        pass
    def describe(self):
        print("brand:",self.brand)
        print("model:",self.model)
    @classmethod
    def from_type(cls,device_type):
        if device_type== "Laptop":
            return Laptop()
        elif device_type== "Smartphone":
            return Smartphone()

class Laptop(ElectronicDevice):
    def __init__(self):
        super().__init__()
        self.power_consumption_rate=50
        try:
            self.battery_life=float(input("enter battery life in hours:"))
        except ValueError:
            print("enter valid battery life in hours")
    def power_usage(self):
        print("power consumption per hour of usage : ",self.power_consumption_rate," watts per hour")
    def describe(self):
        super().describe()
        print("battery life: ",self.battery_life,"hours")
class Smartphone(ElectronicDevice):
    def __init__(self):
        super().__init__()
        self.power_consumption_rate = 10
        try:
            self.screen_size =float(input("enter screen size in inches:"))
        except ValueError:
            print("enter valid screen size in inches")
    def power_usage(self):
        print("power consumption per hour of usage :",self.power_consumption_rate," 10 watts per hour")
    def describe(self):
        super().describe()
        print("screen size: ",self.screen_size,"inches")


smartphone=Smartphone()
smartphone.describe()
smartphone.power_usage()
laptop=Laptop()
laptop.describe()
laptop.power_usage()
device_type=input("enter device type:Laptop,Smartphone ")
if type(device_type) != str or device_type not in("Laptop","Smartphone"):
    print("invalid device type")
else:
    device1=ElectronicDevice.from_type(device_type)
    device1.describe()
