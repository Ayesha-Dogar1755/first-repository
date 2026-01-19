#Program for infinte loop to check number is positive or negative until user type "quit"
while True:
    n=input("Enter a number or type quit:")
    if n=="quit":
        break
    num=int(n)
    if num>0:
        print("Positive number.")
    elif num<0:
        print("Negative number.")
    else:
        print("Zero.")