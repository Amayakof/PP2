# Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
print("-Task 1-")
import re

pattern1 = re.compile(r"ab*")

print("Task 1")
print(pattern1.search("abbba"))