#Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt
import os 
import string 

alphabet = 'Files' 
if not os.path.exists(alphabet): 
    os.makedirs(alphabet) 
 
for letter in string.ascii_uppercase: 
    name = os.path.join(alphabet, letter + '.txt') 
 
    with open(name, 'w') as f: 
        pass 
 
    print("done!") 