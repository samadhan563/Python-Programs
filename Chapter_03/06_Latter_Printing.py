# Program for letter writing
'''
    Author : Samadhan Gaikwad.
    Software Developer
    Location: Pune.
'''

#Concat string two string
string='''Dear <|NAME|>,\n\t Welcome to nuvolo solution, you are selected for trainee devloper.\nThanks!
'''
name=input("Enter name : \n")
string=string.replace("<|NAME|>",name)
print(string)


#---------------------------------------------------------------------------------------------
#       Output
'''
    D:\E-DAC Data\Python\Chapter_03>python 06_Latter_Printing.py
    Enter name :
    Samadhan
    Dear Samadhan,
            Welcome to nuvolo solution, you are selected for trainee devloper.
    Thanks!

'''
#---------------------------------------------------------------------------------------------




