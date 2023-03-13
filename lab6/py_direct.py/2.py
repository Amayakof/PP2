#Write a Python program to check for access to a specified path. Test the existence, readability, writability and executability of the specified path
import os 

#path = input("Please enter the path: ")
path = '/Users/amayakof/Desktop/PP2/lab6/file.txt' 

if os.access(path, os.F_OK): 
    print("It exists") 
else: 
    print("It doesn't exist") 
 
if os.access(path, os.R_OK): 
    print("Readable") 
else: 
    print("Can't read") 
 
if os.access(path, os.W_OK): 
    print("Writable") 
else: 
    print("Can't write") 
 
if os.access(path, os.X_OK): 
    print("Can execute") 
else: 
    print("Can't execute") 
