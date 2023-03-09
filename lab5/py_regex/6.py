# Write a Python program to replace all occurrences of space, comma, or dot with a colon.
print("-Task 6-")
import re

pattern6 = re.compile(r"[ ,.]")

text = "gfdjf,fhdsjh..fdskjf fjhgerj,. fds"
print(pattern6.sub(":", text))