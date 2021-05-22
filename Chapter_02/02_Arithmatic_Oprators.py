#-------------------------------------------------------------------------------------------------------
#      Heading
#Python program for Oprators
'''
    Author : Samadhan Gaikwad.
    Software Developer
    Location: Pune.
'''
#-------------------------------------------------------------------------------------------------------
#       Program 

integerNum1=21
integerNum2=10
integerResult=None

integerResult=integerNum1+integerNum2
print("Addition Of Two Number --->", integerResult) 
print("type of integerResult--->",type(integerResult),"\n")

integerResult=integerNum1-integerNum2
print("Substraction Of Two Number --->", integerResult)
print("type of integerResult--->",type(integerResult),"\n")

integerResult=integerNum1*integerNum2
print("Multiplication Of Two Number --->", integerResult) 
print("type of integerResult--->",type(integerResult),"\n")

integerResult=integerNum1/integerNum2
print("Division Of Two Number --->", integerResult) 
print("type of integerResult--->",type(integerResult),"\n")

integerResult=integerNum1%integerNum2
print("Moduls Of Two Number --->", integerResult) 
print("type of integerResult--->",type(integerResult),"\n")




#-------------------------------------------------------------------------------------------------------
#       Output
'''
    D:\E-DAC Data\Python\Chapter_2>python 02_Oprators.py
    
    Addition Of Two Number ---> 31
    type of integerResult---> <class 'int'>

    Substraction Of Two Number ---> 11
    type of integerResult---> <class 'int'>

    Multiplication Of Two Number ---> 210
    type of integerResult---> <class 'int'>

    Division Of Two Number ---> 2.1
    type of integerResult---> <class 'float'>

    Moduls Of Two Number ---> 1
    type of integerResult---> <class 'int'>

'''

#-------------------------------------------------------------------------------------------------------
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
#End
#-------------------------------------------------------------------------------------------------------