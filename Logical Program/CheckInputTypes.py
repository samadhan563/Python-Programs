# Program for ASCII Value pattern
'''
    Author : Samadhan Gaikwad.
    Software Developer
    Location: Pune.
'''

char=(input("Enter char : charactor"))
# char2=(input("Enter char1 : "))
if char>='A' and char <='Z':
    print(char, "is a upper case charactor.")
elif char>='a' and char <='z':
    print(char, "is a lower case charactor.")
elif char>='0' and char <='9':
    print(char, "is a digit charactor.")
else:
    print(char, "is a special charactor.")
    
