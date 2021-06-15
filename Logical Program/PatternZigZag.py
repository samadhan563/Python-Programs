# Program for Z pattern
'''
    Author : Samadhan Gaikwad.
    Software Developer
    Location: Pune.
'''
n = 7
count = 0
for i in range(n+1):
    for j in range(1,n-i):
        if(j%2==0):
            count+=1
            print(count,end="")
        else:
            print("*",end="")
 
 