# Program for string function in python
'''
    Auther : Samadhan Gaikwad.
    Software Devloper
    Location: Pune.
'''

#Concat string two string
string1="Welcome to Python World !!!"
print("String length : ",len(string1))
print("String end with : ",string1.endswith("!!!"))
print("Check count of o :",string1.count("o"))
print("Capitalize string : ",string1.capitalize())
print("find string : ",string1.find("World")) #return first occurence of World
print("find string : ",string1.replace("World","Learning"))

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



