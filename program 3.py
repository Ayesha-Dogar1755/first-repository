#Taking input from user , check data type and give output
name=input("Enter your name:")
age=int(input("Enter your age:"))  #input always take string.That's why we should use to convert numbers in int.
height=int(input("Enter your height:"))  #input always take string.That's why we should use to convert numbers in int.
edu=input("Enter your Qualification:")
institute_name=input("Enter your college/University name:")
degree=input("Enter your degree:")
print("Name:",name,type(name))
print("Age:",age,type(age))
print("Height:",height,type(height))
print("Education:",edu,type(edu))
print("Institute Name:",institute_name,type(institute_name))
print("Degree:",degree,type(degree))

