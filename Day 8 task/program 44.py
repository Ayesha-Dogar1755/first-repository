# function to show even numbers:
list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
#function definition:
def even_num(list):
    for i in list:
        if i%2==0:
            print("Even number is:",i)
#function calls:
output=even_num(list)
print(output)