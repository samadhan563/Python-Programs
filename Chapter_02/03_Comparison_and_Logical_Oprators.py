# -------------------------------------------------------------------------------------------------------
#      Heading
# Python program for Comparison and Logical Oprators
'''
    Author : Samadhan Gaikwad.
    Software Developer
    Location: Pune.
'''
# -------------------------------------------------------------------------------------------------------
#       Program
# Comparison operators
a = (10 > 20)
print(a)
a = (10 < 20)
print(a)
a = (10 != 20)
print(a)
a = (10 == 20)
print(a)
a = (10 >= 20)
print(a)

# Logical operators
bool1 = True
bool2 = False
print("Bool1 and Bool2 = ",bool1 and bool2)
print("Bool1 and Bool2 = ",bool1 or bool2)

print("Bool1 and Bool2 = ",not bool2)

# -------------------------------------------------------------------------------------------------------
#       Output
'''
   D:\E-DAC Data\Python\Chapter_2>python 03_Comparison_and_Logical_Oprators.py
    False
    True
    True
    False
    False
    Bool1 and Bool2 =  False
    Bool1 and Bool2 =  True
    Bool1 and Bool2 =  True
'''

# -------------------------------------------------------------------------------------------------------
#       Notes
'''
---> Variables-  Container to store a value.
    A variable is the name given to a memory location in a program 
    example:
        a=30 .....a is variable    
        b="Python"  


    ->Python is fantastic language that automatcally identifies the type of data for us.
            str="Hello, i am python"    ->automatcally identifies as String
            integerNum=10               ->automatcally identifies as int
            floatNum=20.20              ->automatcally identifies as float
            booleanVar= True            ->automatcally identifies as boolean
            noneVar=None                ->automatcally identifies as none  
        
    ->Rule for defining the variable name
            -- The variable name can contains alphabets, digit, and underscore. e.g. a_101(Ok)
            -- A variable name can start with alphabate or underscore.   e.g.- abc101 or _abc(Ok)
            -- A variable name can't start with number.     e.g.- 1str="Hello, i am python"(SyntaxError: invalid syntax)
            -- No white spaces allowed inside a variable.   e.g. nu m=10 (SyntaxError: invalid syntax)

            note: variable name are case sensitive..

---> Keyword-    Reserved word in python.

        False      await      else       import     pass
        None       break      except     in         raise
        True       class      finally    is         return
        and        continue   for        lambda     try
        as         def        from       nonlocal   while
        assert     del        global     not        with
        async      elif       if         or         yield
---> Identifiers-The specific mark for identifying the that specific element. every name is called as indentifiers.

---> Datatypes:
        1.Integer
        2.Floating Point numbers.
        3.String---Collection of characters enclosed in single code or double code or triple code also in python.
        4.Boolean. e.g-true or false. (in hindi such ya jhutt)
        5.None. ---This variable used for represent the nothing.(in hindi kuch bhi nahi !)) 

---> Oprators in Python.
        ->Common types of oprators.
            1.Arithmatic oprators :> +, -, *, /, etc.
            2.Assignment oprators :> =, -=, +=, /=, etc.
            3.Comparison oprators :> ==, <, >, <=, >=, !=, etc.
            4.Logical oprators    :> and, or, not, etc.
            

'''
# End
# -------------------------------------------------------------------------------------------------------
