import Employee

emp = []
count = int(input("Enter List size : "))
for i in range(1, count+1):
    print("Enter details like : First Name, Last name, Salary")
    id=int(i)
    firstName=str(input())
    lastName=str(input())
    salary=float(input())
    emp[i]=Employee(id,firstName,lastName, salary)
for e in emp:
    print(e.toString())
    
