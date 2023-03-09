#Write a Python program to count the number of lines in a text file.
import os 

#path = input("Please enter the path: ")
path = '/Users/amayakof/Desktop/PP2/lab6/file.txt' 

with open(path, 'r') as f: 
    cnt = 0 
    for line in f: 
        cnt += 1 
 
print(cnt) 
