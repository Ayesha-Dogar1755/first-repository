class Person:
    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Address:",self.address)
person1=Person("Alice",30,"123 Main St")
person1.display()
