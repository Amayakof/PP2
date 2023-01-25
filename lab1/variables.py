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
