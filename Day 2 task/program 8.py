# Program to check whether a character is an alphabet,digit o special character
ch=input("Enter a character:")
if (ch>='a' and ch<='z') or (ch>= 'A' and ch<= 'Z'):
    print(f"{ch} is an alphabet")
elif ch>= '0' and ch<= '9':
    print(f"{ch} is a digit.")
else:
    print(f"{ch} is a special character.")