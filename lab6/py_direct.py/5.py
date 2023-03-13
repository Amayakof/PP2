#Write a Python program to write a list to a file.
list = ['hello', ',', 'this', 'is', 'lab', 'work', 'number', 'six'] 
 
path = input("Name: ") 
 
with open(path, 'w') as file: 
 
    for s in list: 
        file.write(s + ' ') 

file.close()
print("The list is in the file ", path) 