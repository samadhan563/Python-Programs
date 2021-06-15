# Program for if else in python
'''
    Author : Samadhan Gaikwad.
    Software Developer
    Location: Pune.
'''

# ---------------------------------------------------------------------------------------------
#       Program
words = ['nashik', 'pokhri']
with open("data.txt", ) as f:
    content = f.read()
    print(content)
for word in words:
    with open("data.txt", 'w') as f:
        content = content.replace(word, '######')
        print(content)
        f.write(content)
print("Done")

# ---------------------------------------------------------------------------------------------
#       Output
'''
    D:\E-DAC Data\Python\Chapter_06>python 05_FileContent.py
    samadhan nana gaikwad at post pokhri tal nandgaon dist nashik
    samadhan nana gaikwad at post pokhri tal nandgaon dist ######
    samadhan nana gaikwad at post ###### tal nandgaon dist ######
    Done 
'''
# ---------------------------------------------------------------------------------------------
