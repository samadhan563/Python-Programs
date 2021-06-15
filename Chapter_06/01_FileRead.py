# Program for if else in python
'''
    Author : Samadhan Gaikwad.
    Software Developer
    Location: Pune.
'''

# ---------------------------------------------------------------------------------------------
#      Program
f = open("intro.txt", 'r')
'''data = f.read()
# read all data
print(data)
# read first 5 char
print("read first 6 char", f.read(6))'''
while (True):
    line=f.readline()
    if line=="":
        break
    print(line,end="")



# ---------------------------------------------------------------------------------------------
#       Output
'''
    Hello,
        I'm Samadhan Nana Gaikwad from pune, I'm BE graduated in computer engineering in 2018
    with First Class recently i completed my CDAC achievement specialized in DAC.
'''
# ---------------------------------------------------------------------------------------------
