# Write a Python program that matches a string that has an 'a' followed by two to three 'b'.
print("-Task 2-")
import re

pattern2 = re.compile(r"ab{2,3}")

print(pattern2.search("gjdfkabbbbfkkliu"))