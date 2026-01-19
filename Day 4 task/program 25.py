# Program to implement a number guessing game
secret=7
while True:
    guess=int(input("Enter your guess:"))
    if guess>secret:
        print("Too high")
    elif guess<secret:
        print("Too low")
    elif guess==secret:
        print("Correct!")
        break