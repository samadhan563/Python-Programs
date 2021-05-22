# Program for find word in python
'''
    Author : Samadhan Gaikwad.
    Software Developer
    Location: Pune.
'''
#-----------------------------------------------------------------------------------------------------------------------
#       Program
line=input()
word=input()
location=line.find(word)
if(location==-1):
    print("NOT FOUND")
else:
    # sub=line[location:len(line)]
    #last=line.find(".",location)
    print(line[location:((line.find(".",location))+1)])
#-----------------------------------------------------------------------------------------------------------------------
#       Output
'''
    D:\E-DAC Data\Python\Logical Program>python FindString.py
    additionl text to be display in details pain of test log. details can hold data of any type comatable with OLE. If it cannot be converted to text, its value is ignored. pmLowest is set to 100. pmHigh
    pmLowest
    pmLowest is set to 100.
'''
