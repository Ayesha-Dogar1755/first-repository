# Program to count the number of digits in a number
n=int(input("Enter a number:"))
count=0 # initialize count to 0
while n>0:
    digit=n%10
    count=count+1
    n=n//10
print("Total digits:",count)