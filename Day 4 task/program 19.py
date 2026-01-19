# Program to print digits of a number in reverse order
n=int(input("Enter a number:"))
while n>0:
    digit=n%10 # get the last digit
    print(digit)
    n=n//10 # remove the last digit