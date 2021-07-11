# Program for if else in python
'''
    Author : Samadhan Gaikwad.
    Software Developer
    Location: Pune.
'''

# ---------------------------------------------------------------------------------------------
#  Program

from Employee import Employee
# Single object of employee
# id = int(input())
# firstName = str(input())
# lastName = str(input())
# salary = float(input())
# emp= Employee(id, firstName, lastName, salary)
# print(emp.toString())

# array of object of employee
emp = []
count = int(input("Enter List size : "))
for i in range(1, count+1):
    print("Enter details like : First Name, Last name, Salary")
    id = int(i)
    firstName = str(input())
    lastName = str(input())
    salary = float(input())
    emp.append(Employee(id, firstName, lastName, salary))
    # emp[i]=Employee(id, firstName, lastName, salary)
    i += 1
for e in emp:
    print(e.toString())

# ---------------------------------------------------------------------------------------------
#  Output
'''
    PS D:\E-DAC Data\Python> & C:/Users/samad/AppData/Local/Programs/Python/Python39/python.exe "d:/E-DAC Data/Python/Chapter_07/01_Employee.py"
    Enter List size : 2
    Enter details like : First Name, Last name, Salary
    aaaaa
    aaaaa
    22222
    Enter details like : First Name, Last name, Salary
    sssss
    sssss
    33333 
    Emp Id : 1
    Emp First Name : aaaaa
    Emp Last Name         : aaaaa
    Emp Salary : 22222.0
    Emp Id : 2
    Emp First Name : sssss
    Emp Last Name         : sssss
    Emp Salary : 33333.0
'''
