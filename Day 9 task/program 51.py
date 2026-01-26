from abc import ABC,abstractmethod

class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

class Intern(Employee):
    def calculate_salary(self):
        return 15000
class FullTimeEmployee(Employee):
    def calculate_salary(self):
        return 50000
class ContractEmployee(Employee):
    def calculate_salary(self):
        return 40000    
intern1=Intern()
print("Intern Salary:",intern1.calculate_salary())
fulltime1=FullTimeEmployee()
print("Full Time Employee Salary:",fulltime1.calculate_salary())
contract1=ContractEmployee()
print("Contract Employee Salary:",contract1.calculate_salary())    