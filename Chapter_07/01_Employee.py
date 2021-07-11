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
