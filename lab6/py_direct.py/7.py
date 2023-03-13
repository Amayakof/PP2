#Write a Python program to copy the contents of a file to another file
import os 
 
first = '/Users/amayakof/Desktop/PP2/lab6/first.txt' 
second = '/Users/amayakof/Desktop/PP2/lab6/second.txt' 
with open(first, 'r') as f: 
    x = f.read() 
 
with open(second, 'w') as n: 
    n.write(x) 
 
print("Done!") 