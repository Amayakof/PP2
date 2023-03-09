# Write a Python program to find the sequences of one upper case letter followed by lower case letters.
print("-Task 4-")
import re

pattern4 = re.compile(r"[A-Z]{1}[a-z]+")

print(pattern4.findall("HasjHa HTAsjh YdTtKsg"))