# Program for Set methods in python
'''
    Author : Samadhan Gaikwad.
    Software Developer
    Location: Pune.
'''
# non repetative element. unordered, cannot access by index
# create set
# a={} this syntax create empty dictonary
# a=() this syntax create empty set
setOfInteger={10,20,30,40,50,10,20,60}
print(setOfInteger)
setOfInteger.add(70)
print(setOfInteger)#you cant add list in set bcz list and dictonary not hashable
print(len(setOfInteger))
setOfInteger.remove(50)#remove particuler element
print(setOfInteger)
print(setOfInteger.pop())#return one element

user={2044,"Samadhan",9527644283}
user.add("abc")
print(user)

# ---------------------------------------------------------------------------------------------
#       Output
'''

'''
# ---------------------------------------------------------------------------------------------
