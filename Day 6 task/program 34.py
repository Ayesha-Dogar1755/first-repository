# ask user to input names of their three favorite fruits and store them in a list. Then, print the list.
favorite_fruits = []
for i in range(3):
    fruit = input("Enter the name of one of your favorite fruits: ")
    favorite_fruits.append(fruit)
print("Your favorite fruits are:", favorite_fruits)    