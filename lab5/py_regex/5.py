# Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
print("-Task 5-")
import re

print("Write something :)")
txt = input()
pattern5 = re.compile(r"a.+b\Z")
   
print(pattern5.search(txt))