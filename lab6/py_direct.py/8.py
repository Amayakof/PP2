#Write a Python program to delete file by specified path. Before deleting check for access and whether a given path exists or not.
import os 
 
path = '/Users/amayakof/Desktop/PP2/lab6/py_func.txt' 
 
if os.path.exists(path)and os.access(path, os.F_OK): 
    os.remove(path) 
    print("done!") 
else: 
    print("file does not exist")