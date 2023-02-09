Functions
Lambda
Classes/Objects
Inheritance

Functions:
A function is a block of code which only runs when it is called.

You can pass data, known as parameters, into a function.

A function can return data as a result.

def my_function():
print("Hello from a function)

#Calling a function
my_function()

#Arguments
Information can be passed into functions as arguments.

!!!Arguments are specified after the function name, inside the parentheses. 
You can add as many arguments as you want, just separate them with a comma.

!!!Parameters vs arguments:
Parameter is given in the def of function
Argument is sent to the func when it is called

!Arbitrary arguments *name:
When you don't know how many arguments are given, 
add * before parameter name:

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

!Keyword arguments:
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

!You can also give a default parameter value: 
def my_function(country = "Norway"):
    print("I am from", country )

my_function()

!You can pass a list as an argument, using for loop
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

!use return to return values of function
def my_function(x):
    return x * 5

print(my_function(3))
print(my_function(5))
print(my_function(9))

!!!Function definitions can't be empty, use pass to avoid the error

#Recursion:


#Lambda function:
A lambda function is a small anonymous function.

A lambda function can take any number of arguments, but can only have one expression.

x = lambda a, b : a * b
print(x(5, 6))

#Class/Objects
Almost everything in Python is an object, with its properties and methods.

A Class is like an object constructor, or a "blueprint" for creating objects.

To create a class use "class"
class My_class:
    x = 5

!Create object:
p1 = My_Class()
print(p1.x)

!The __init__() Function
- Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created

__init__() funcrion is called automatically every time class is being used to create new onject

!The __str__() Function
- The __str__() function controls what should be returned when the class object is represented as a string.