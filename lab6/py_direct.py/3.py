#Write a Python program to test whether a given path exists or not. If the path exist find the filename and directory portion of the given path.
import os 

#path = input("Please enter the path: ")
path = '/Users/amayakof/Desktop/PP2/lab6/text.txt' 
 
if os.access(path, os.F_OK): 
    print("exists") 
    print(os.path.basename(path)) 
    print(os.path.dirname(path)) 
else: 
    print("doesn't exist") 
 
if os.path.exists(path): 
    print(f'{path} exists') 
    print(os.path.basename(path)) 
    print(os.path.dirname(path)) 
else: 
    print(f'{path} does not exist') 
 
