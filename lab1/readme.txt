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
Print the data type of the variable x:
x = 5
print(type(x))

#int
x = 5
print("int type example: ", x)

#float
x = 5.678
print("float type example: ", x)

#complex
#Complex numbers are written with a "j":
x = 5j + 5
print("complex type example: ", x)

#type conversions
-complex type number can't be converted into another type
x = 5
print("Int: ", x)

a = float(x)
print(type(a))

y = 4.565786
print("Float: ", y)

b = int(y)
print(type(b))

#random -> module
import random
print(random.range(1, 19))

#Python Numbers
numeric types:
-int
-float
-complex

#Python casting
float type into int at input process
x = int("3), x will be 3
y = int(3.554456), y will be 3
z = float(1), z will be 1.0
i = str(3.0), i will be '3.0'

#Python Strings
strings '', ""
print("hello") or ('hello')

- assign str as variable:
a = "hello"
print(a)

- multiline strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

or 
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)
-in the result, 
the line breaks are inserted at the same position as in the code.

-Strings are arrays
a = "Hello, World!"
print(a[1])
result: e

-Looping through a string
for x in "banana":
  print(x)

-String lenght
a = "Hello, world"
print(len(a))

-Check String
txt = "Free cheese is in the claw of a lie"
print("free" in txt)

combine with if statement
txt = "Free cheese is in the claw of a lie"
if "free" in txt:
    print("Warning!")

-If NOT
txt = txt = "Free cheese is in the claw of a lie"
print("Safe" not in txt)

combine with if
txt = "Free cheese is in the claw of a lie"
if "free" not in txt:
    print("Safe")

#Slicing string
b = "Hello, World!"
print(b[2:5]) -> range of Slicing

use slice from Start
print(b[:5])

slice to the end
print(b[2:])

Negative indexing
print(b[-5:-2])

-Modify strings
upper() method
a = "Hello, world"
print(a.upper())

lower() method
print(a.lower())

-Remove Whitespace
a = " Hello, world "
print(a.strip())
returns "Hello, World"

-Replace string
a = "Hello, world"
print(a.replace("H", "J"))

-Split string
a = "Hello, world"
print(a.split(","))
return: ['Hello', 'World']

-String Concatenation
a = "Hello"
b = "world"
c = a + b
print(c)

-add space
c = a + " " + b
print(c)

-Format Strings
-to combine string with numbers
age = 17
txt = "My name is Zhaniya, and I am {}"
print(txt.format(age))

can use indexes
age = 17
bday = 21
month = 9
myformat = "My name is Zhaniya, my birthday is {1}, {2}, I am {0} y.o"
print(myorder(format(age, bday, month)))

-Escape characters
txt = "We are the so-called \"Vikings\" from the north."

-Strings Methods
All string methods return new values, 
they don't modify the original string

*capitalize()
*find()
*format()
*index()

#Booleans
-True or False values

x = "Hello"
y = 15

print(bool(x))
print(bool(y))

-Any value except 0 is True
-Any string is True except empty
-Any list is True except empty

Functions can return bool values

#Python Operators
Unusual cases:
-Exponentiation: 2**3 -> 8
-Floor division: 15//2 -> 7
-and(instead of &); or(inst-d of ||)
-is; is not
Bitwise:
-Not: ~x

#If...Else
-If...else
a = 2
b = 330
print("A") if a > b else print("B")
-shorthand version

-elif
another condition if "if" didn't work

-pass
If the statement is empty