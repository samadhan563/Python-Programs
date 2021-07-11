class Employee:
    id = 0
    firstName = ""
    lastName = ""
    salary = 0.0

    def __init__(self):
        id = 0
        firstName = None
        lastName = None
        salary = 0.0

    def __init__(self, id, firstName, lastName, salary):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.salary = salary

    def toString(self):
        return f"Emp Id : {self.id} \nEmp First Name : {self.firstName} \nEmp Last Name\
         : {self.lastName} \nEmp Salary : {self.salary}"


# id = int(input())
# firstName = str(input())
# lastName = str(input())
# salary = float(input())
# emp= Employee(id, firstName, lastName, salary)
# print(emp.toString())
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
    # print(e)
