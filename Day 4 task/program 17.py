# Program to print all even numbers in a given range
num_1=int(input("Enter first number:"))
num_2=int(input("Enter second number:"))
for i in range(num_1,num_2+1):
    if i%2==0:
        print(i)