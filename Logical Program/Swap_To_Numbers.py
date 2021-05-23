# Program for Z pattern
'''
    Author : Samadhan Gaikwad.
    Software Developer
    Location: Pune.
'''

def swap(x,y):
    x=x+y
    y=x-y
    x=x-y
    return {x,y}
a=10 
b=20
print(a," ",b)
a,b=swap(a,b)
print(a," ",b)

