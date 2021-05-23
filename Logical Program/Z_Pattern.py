# Program for Z pattern
'''
    Author : Samadhan Gaikwad.
    Software Developer
    Location: Pune.
'''

for i in range(7):
    for j in range(7):
        if i==0 or i==6:
            print("*",end="")
        elif j==7-i:
            print("*",end="")
        else:
            print(" ",end="")
    print()
    
