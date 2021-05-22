# Program for Prime Number from list in python
'''
    Auther : Samadhan Gaikwad.
    Software Devloper
    Location: Pune.
'''
#create list 
arr=[10,21,5,1,2,3,4,5,6,7,8,9]
print("Prime number from list : ",end=" ")
for i in range(0,len(arr)):
    count=0
    for j in range(1,arr[i]+1):
        if ((arr[i]%j)==0):
            count+=1
    if(count==2):
        print(arr[i],end=" ")



#---------------------------------------------------------------------------------------------
#       Output
'''
    D:\E-DAC Data\Python\Chapter_04>python 04_DisplayPrimeNumberFromList.py
    Prime number from list :
    5 2 3 5 7
'''
#---------------------------------------------------------------------------------------------





