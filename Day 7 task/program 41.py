#program to take marks of three subjects from user and store them in a dictionary
marks = {}
x=int(input("Enter marks for phy: "))
y=int(input("Enter marks for chem: "))
z=int(input("Enter marks for math: "))
marks["phy"] = x
marks["chem"] = y
marks["math"] = z
print("Marks dictionary:", marks)