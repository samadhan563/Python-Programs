# Program for string slicing in python
'''
    Auther : Samadhan Gaikwad.
    Software Devloper
    Location: Pune.
'''

#Concat string two string
string1="Python"
string1="Welcome to "+string1+" World !!!"
print(string1)
#String Slicing
string1="Python"
print(string1[2])
print("String Slicing ",string1[0:3])#including 0 and excluding 3
print("String Slicing ",string1[3:6])#including 3 and excluding 6
print("String Slicing ",string1[:4])#including 0 and excluding 4(0 to 3) same as(0:4)
print("String Slicing ",string1[2:])#including 3 and excluding 6(3 to 6)same as(3:6) 

#---------------------------------------------------------------------------------------------
#       Output
'''
    D:\E-DAC Data\Python\Chapter_03>python 02_String_Program_Slicing.py
    Welcome to Python World !!!
    t
    String Slicing  Pyt
    String Slicing  hon
    String Slicing  Pyth
    String Slicing  thon
'''
#---------------------------------------------------------------------------------------------
#       Notes
'''
    String Slicing
    ->  A String in python can be sliced for getting a part of the string. length-1 otherwise error string out of range.
    ->  string1[2]="A"---Not work
    ->  index start from 0 to length-1
'''



