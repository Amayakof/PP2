What is Python?
Python is a popular programming language. It was created by Guido van Rossum, and released in 1991.

It is used for:

web development (server-side),
software development,
mathematics,
system scripting.

What can Python do?
Python can be used on a server to create web applications.
Python can be used alongside software to create workflows.
Python can connect to database systems. It can also read and modify files.
Python can be used to handle big data and perform complex mathematics.
Python can be used for rapid prototyping, or for production-ready software development.


Python Intro
Python User Input
Python Get Started
Python Syntax
Python Comments
Python Variables
Python Data Types
Python Numbers
Python Casting
Python Strings
Python String Formatting
Python Booleans
Python Operators
Python If...Else
Git

Syntax
if 5 > 2:
  print("Five is greater than two!")
#syntaxis requires spaces devisions(>1, commonly used: 4)

#comments
"""if 5 > 2:
  print("multiline string that is ignored")"""


Variables
#Variables
#Python has no command for declaring a variable.
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

#If you want to specify the data type of a variable, this can be done with casting.
x = str(3) 
y = int(3)    
z = float(3)  

#type() function
a = 'Z'
b = 2005
print(type(a))
print(type(b))

##Variables
#Python has no command for declaring a variable.
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

#If you want to specify the data type of a variable, this can be done with casting.
x = str(3) 
y = int(3)    
z = float(3)  

#Variables names
myvar = "Zhaniya"
my_var = "Zhaniya"
_my_var = "Zhaniya"
myVar = "Zhaniya"
MYVAR = "Zhaniya"
myvar2 = "Zhaniya"
#don't use num as first symb of a var, don't use symbols other than _, don't use spaces

#Multi words variables
"""
-Camel case(myVarName)
-Pascal case(MyVarName)
-Snake case(my_var_name)"""

#Many Values to Multiple Variables
#number of variables matches the number of values
x, y, z = "Zhaniya", "Koshkimbayeva", "Erdosqyzy"
print(x)
print(y)
print(z)

#also if use x = y = z = "Zhaniya", all var are equal

#Unpacking collection
fruits = ["Zhaniya", "Koshkimbayeva", "Erdosqyzy"]
x, y, z = fruits
print(x)
print(y)
print(z)

#Output variables
#by putting many variables into one print, can print multiple var
x = "Koshkimbayeva "
y = "Zhaniya "
z = "Yerdosqyzy"
print(x, y, z)
#also can use + instead
#can't combine different types in the print() funct by using "+", use "," inst

#Global Variables
#Variables that are created outside of a function
x = "Student"

def myfunc():
  x = "Zhaniya"
  print("Info: " + x)

myfunc()

print("Info: " + x)

#use the global keyword -> the variable belongs to the global scope
def myfunc():
  global x
  x = "Student"

myfunc()

print("Info: " + x)

#use the global keyword -> change a global variable inside a function
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#Python Data types

