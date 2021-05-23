# Program for dictionary methods in python
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
print("Roll Number  : ", dict["rollNum"])  # key must present in dictionary
print("Name         : ", dict["firstName"], " ", dict["lastName"])
print("Mob Number   : ", dict["mobNumber"])
print("Qualification: \n\t\tGraduate \t:",
      dict["qualification"]["graduate"], "\n\t\tSpecialization\t:", dict["qualification"]["specialization"])
print(list(dict.keys()))  # print values associated with key
print(dict.values())
print(dict.items())  # key, value pair for all contains
dictUpdate = {
    "location": "Pune"
}
# update the dictonery by by adding key-value pairs from dictUpdate also update existing key
dict.update(dictUpdate)
print(dict)

print(dict.get("firstName"))  # if key is not found return none


# ---------------------------------------------------------------------------------------------
#       Output
'''

'''
# ---------------------------------------------------------------------------------------------
