#Program to check if a list contains a palindrome of elements
list=[1,2,3,2,1]
copy_of_list=list.copy() #create a copy of original list
copy_of_list.reverse() #reverse the copy
if list==copy_of_list:
    print("The list is a palindrome.")
else:
    print("The list is not a palindrome.")