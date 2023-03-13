#Write a Python program to list only directories, files and all directories, files in a specified path. 
import os 

path = input("Please enter the path: ")
#path = '/Users/amayakof/Desktop/PP2/lab6' 
 
print("Directories: ") 
for direct in os.listdir(path): 
    if os.path.isdir(os.path.join(path, direct)): 
        print(direct) 
 
 
print("\nFiles: ") 
for file in os.listdir(path): 
    if os.path.isfile(os.path.join(path, file)): 
        print(file) 
 
 
print("\nAll directories and files: ") 
for all in os.listdir(path): 
    print(all) 