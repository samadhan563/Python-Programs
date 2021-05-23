# Program for average of tuple elements in python
'''
    Author : Samadhan Gaikwad.
    Software Developer
    Location: Pune.
'''
# non repetative element. unordered, cannot access by index
# create set
# a={} this syntax create empty dictonary
# a=() this syntax create empty set
numbers=(10,20,30,40,50,10,20,60)
def average(t):
    sum=0
    for i in t:
        sum+=i
    return sum/len(t)
print(average(numbers))
# ---------------------------------------------------------------------------------------------
#       Output
'''

'''
# ---------------------------------------------------------------------------------------------
