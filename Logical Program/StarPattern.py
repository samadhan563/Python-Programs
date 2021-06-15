# Program for Z pattern
'''
    Author : Samadhan Gaikwad.
    Software Developer
    Location: Pune.
'''
n = 3
for i in range(3):
    print(" "*(n-i-1), end="")
    print("*"*(2*i+1), end="")
    print(" "*(n-i-1))
