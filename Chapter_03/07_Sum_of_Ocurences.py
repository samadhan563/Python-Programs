# Program for sum of prime occurences
'''
    Author : Samadhan Gaikwad.
    Software Developer
    Location: Pune.
'''

# Concat string two string
string = input("Enter string : ")
occurences = []
counter=0 
sum=0
product=1
i=0
#Find occurences
while(True):
    if(len(string)!=0):
        occurences.append(string.count(string[i]))
        string=string.replace(string[i],"")
        counter=counter+1    
    else :
        break
#Prime occurences
for i in range(0, len(occurences)):
    prime=0
    for j in range(1, occurences[i]+1):
        if((occurences[i]%j)==0):
            prime+=1  
    if(prime==2):
        sum+=occurences[i]
        product*=occurences[i]
    
print("sum = ",sum)
print("product = ",product)

# ---------------------------------------------------------------------------------------------
#       Output
'''
    D:\E-DAC Data\Python\Chapter_03>07_Sum_of_Ocurences.py
    Enter string : abcdefabcdefabcdefabcdefabcdef
    sum =  30
    product =  15625


'''
# ---------------------------------------------------------------------------------------------
