# Program to filter even numbers from a list
list=[1,2,3,4,5,6,7,8,9,10]
even_numbers=[]
for i in list:
    if i%2==0:
        even_numbers.append(i)
print("Even numbers in the list are:", even_numbers)        