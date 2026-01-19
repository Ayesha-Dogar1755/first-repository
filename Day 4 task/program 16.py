# Program to calculate tax based on salary
salary=int(input("Enter your salary:"))
if salary<30000:
    tax=salary*5/100 
    print("Your tax is:",tax)
elif salary >=30000 and salary<=70000:
    tax=salary*15/100
    print("Your tax is:",tax)
elif salary>70000:
    tax=salary*25/100
    print("Your tax is:",tax)