#Program takes a list from user and print sum of all elements
user_list = []
n = int(input("Enter the number of elements you want in the list: "))
for i in range(n):
    value=input("enter the value:")
    user_list.append(value)
print("The list you entered is:", user_list)
sum_of_elements = 0
for value in user_list:
    sum_of_elements+=int(value)
print("The sum of all elements in the list is:", sum_of_elements)
