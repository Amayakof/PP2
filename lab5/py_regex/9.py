# Write a Python program to insert spaces between words starting with capital letters.
print("-Task 9-")
import re

def spaces(text):
    res = ""
    pattern = re.compile(r"[A-Z][a-z]+")
    words = pattern.findall(text)
    for i, word in enumerate(words):
        if i != 0:
            res += " " + word
        else:
            res += word
    return res

print(spaces("LoremIpsumHere"))