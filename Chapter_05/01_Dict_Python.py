# Program for dictionary in python
'''
    Author : Samadhan Gaikwad.
    Software Developer
    Location: Pune.
'''
# create list
dict = {
    "rollNum": 2044,
    "firstName": "Samadhan",
    "lastName": "Gaikwad",
    "mobNumber": 9527644283,
    "qualification": {
        "graduate": "BE",
        "specialization": "Computer Engineering"
    }
}
# print(dict)
print("Roll Number  : ", dict["rollNum"])
print("Name         : ", dict["firstName"], " ", dict["lastName"])
print("Mob Number   : ", dict["mobNumber"])
print("Qualification: \n\t\tGraduate \t:",
      dict["qualification"]["graduate"], "\n\t\tSpecialization\t:", dict["qualification"]["specialization"])
dict["rollNum"]=200941281042
print("Roll Number  : ", dict["rollNum"])


# ---------------------------------------------------------------------------------------------
#       Output
'''

'''
# ---------------------------------------------------------------------------------------------
