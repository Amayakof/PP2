# Write a Python program to find sequences of lowercase letters joined with a underscore.
print("-Task 3-")
import re

pattern3 = re.compile(r"[a-z]+\_")

print(pattern3.findall("fdsfd_ fdjskfjdsk_ fdsf4ds_"))