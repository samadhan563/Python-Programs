# Program for Prime Number in python
'''
    Auther : Samadhan Gaikwad.
    Software Devloper
    Location: Pune.
'''
#create list 
arr=[10,21,5,1,2,3,4,5,6,7,8,9]
print("Serise of 1 to 100 prime number : ")
for i in range(1,101):
    count=0
    for j in range(1,i+1):
        if ((i%j)==0):
            count+=1
    if(count==2):
        print(i)



#---------------------------------------------------------------------------------------------
#       Output
'''

'''
#---------------------------------------------------------------------------------------------




