class Student:
    def __init__(self,name,roll_number,marks):
        self.name=name
        self.roll_number=roll_number
        self.marks=marks
    def set_name(self,name):
        if name:
            self.name=name
        else:
            print("Name cannot be empty.")
    def get_name(self):
        return self.name
    def set_roll_number(self,roll_number):
        if roll_number>0:
            self.roll_number=roll_number
        else:
            print("Roll_number cannot be zero.")
    def get_roll_number(self):
        return self.roll_number
    def set_marks(self,marks):
        if 0<=marks<=100:
            self.marks=marks
        else:
            print("Marks should be between 0 and 100.")   
    def get_marks(self):
        return self.marks

student1=Student("John",1,85)
print("Name:",student1.get_name())
print("Roll Number:",student1.get_roll_number())
print("Marks:",student1.get_marks())                         
    