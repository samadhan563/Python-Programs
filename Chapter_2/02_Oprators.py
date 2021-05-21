#-------------------------------------------------------------------------------------------------------
#      Heading
#Python program for variable
'''
    Auther:Samadhan Nana Gaikwad.
    Location:Pune.
    Company Name:Nuvolo solution pvt. ltd., Pune.
'''
#-------------------------------------------------------------------------------------------------------
#       Program 

str="Hello, i am python" # or str='Hello, i am python' or str='''Hello, i am python'''
integerNum=10
floatNum=20.20
booleanVar= False
noneVar=None

print("String       --->",str) 
print("Integer      --->",integerNum) 
print("Float        --->",floatNum) 
print("Boolean      --->",booleanVar) 
print("None         --->",noneVar)

print("type of str          --->",type(str))
print("type of floatNum     --->",type(floatNum))
print("type of integerNum   --->",type(integerNum))
print("type of booleanVar   --->",type(booleanVar))
print("type of noneVar      --->",type(noneVar))
#-------------------------------------------------------------------------------------------------------
#       Output
'''
    D:\E-DAC Data\Python\Chapter_2>python 01_Variable.py
    String       ---> Hello, i am python
    Integer      ---> 10
    Float        ---> 20.2
    Boolean      ---> True
    None         ---> None
    type of str          ---> <class 'str'>
    type of floatNum     ---> <class 'float'>
    type of integerNum   ---> <class 'int'>
    type of booleanVar   ---> <class 'bool'>
    type of noneVar      ---> <class 'NoneType'>
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