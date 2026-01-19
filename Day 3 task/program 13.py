# Program to search for an element in a list using while loop
list=(1,4,9,16,25,36,49,64,81,100)
x=36
idx=0
while idx<len(list):
    if list[idx]==x:
        print("FOUND!")
    idx+=1