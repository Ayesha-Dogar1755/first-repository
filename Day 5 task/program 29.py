#program to perfor various string operations
str1="apna_college"
#check ending of string
print(str1.endswith("er")) #if words ends with er then true else false
#capitalize first letter of string
print(str1.capitalize()) #Output: Apna college
#convert string to uppercase
print(str1.upper()) #Output: APNA COLLEGE
#convert string to lowercase
print(str1.lower()) #Output: apna college
#count letter in word
print(str1.count("a")) #Output: 2
#replace word in string
print(str1.replace("college","school")) #Output: apna school
#find index of string
print(str1.find("college")) #Output: 5