# Write a Python program to convert a given camel case string to snake case.
print("-Task 10-")
import re

def camel_to_snake(text):
    res = ""
    pattern = re.compile(r"[A-Z][a-z]+")
    words = pattern.findall(text)
    for i, word in enumerate(words):
        if i == 0:
            res += word.casefold()
        else:
            res += "_" + word.casefold()
    return res

print(camel_to_snake("RandomTextRightHere"))