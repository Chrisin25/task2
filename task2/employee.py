from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self):
        self.name=input("enter name of employee: ")
    @abstractmethod
    def calculate_salary(self):
        pass
    def describe(self):
        print("employee name:",self.name)
class FullTimeEmployee(Employee):
    def __init__(self):
        super().__init__()
        self.type="Full time"
        self.salary=3000
    def calculate_salary(self):
        return self.salary
    def describe(self):
        super().describe()
        print("type : ",self.type)
class PartTimeEmployee(Employee):
    def __init__(self):
        super().__init__()
        self.type="part time"
        self.salary=0
    def calculate_salary(self):
        try:
            hours_worked=float(input("enter hours worked: "))
            hourly_rate=float(input("enter hourly rate: "))
            self.salary = hours_worked * hourly_rate
        except ValueError:
            print("Value Exception:enter a valid number")
        return self.salary
    def describe(self):
        super().describe()
        print("type : ",self.type)


full_time_employee=FullTimeEmployee()
full_time_employee.describe()
print("salary:$",full_time_employee.calculate_salary())

part_time_employee=PartTimeEmployee()
part_time_employee.describe()
print("salary:$",part_time_employee.calculate_salary())

