#program to take a list from user using loop
user_list = []
n = int(input("Enter the number of elements you want in the list: "))
for i in range(n):
    value=int(input("enter the value:"))
    user_list.append(value)
print("The list you entered is:", user_list)