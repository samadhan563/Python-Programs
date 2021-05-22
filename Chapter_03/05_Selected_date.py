# Program for name followed by good night
'''
    Author : Samadhan Gaikwad.
    Software Developer
    Location: Pune.
'''

#Concat string two string
string='''Dear <|NAME|>, 
You are selected in nuvolo on <|DATE|>
'''
name=input("Enter name : \n")
date=input("Enter date : \n")
string=string.replace("<|NAME|>",name)
string=string.replace("<|DATE|>",date)
print(string)


#---------------------------------------------------------------------------------------------
#       Output
'''
    D:\E-DAC Data\Python\Chapter_03>05_Selected_date.py
    Enter name :
    samadhan
    Enter date :
    28-05-2021
    Dear samadhan,
    You are selected in nuvolo on 28-05-2021
'''
#---------------------------------------------------------------------------------------------




