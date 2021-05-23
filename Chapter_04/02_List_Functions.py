# Program for List in python
'''
    Author : Samadhan Gaikwad.
    Software Developer
    Location: Pune.
'''
#create list 
arr=[10,21,5,1,2,3,4,5,6,7,8,9]
#Sorting list
arr.sort()
print("Sorted : ",arr)
#Reverse list
arr=[10,21,5,1,2,3,4,5,6,7,8,9]
arr.reverse()
print("After reverse : ",arr)
#append list
arr=[10,21,5,1,2,3,4,5,6,7,8,9]
arr.append(35)#add at the end of list
print("After append : ",arr)

arr.insert(2,101)#insert at the position of list
print("After Insert 101 : ",arr)

arr.pop(2)#remove at the position of list
print("After pop 2 : ",arr)


arr.remove(21)#remove at the position of list
print("After remove 21 : ",arr)

#---------------------------------------------------------------------------------------------
#       Output
'''
    D:\E-DAC Data\Python\Chapter_04>python 02_List_Functions.py
    Sorted :  [1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10, 21]
    After reverse :  [9, 8, 7, 6, 5, 4, 3, 2, 1, 5, 21, 10]
    After append :  [10, 21, 5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 35]
    After Insert 101 :  [10, 21, 101, 5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 35]
    After pop 2 :  [10, 21, 5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 35]
    After remove 21 :  [10, 21, 5, 2, 3, 4, 5, 6, 7, 8, 9, 35]
'''
#---------------------------------------------------------------------------------------------




