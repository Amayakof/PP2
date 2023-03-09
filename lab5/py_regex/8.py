# Write a Python program to split a string at uppercase letters.
print("-Task 8-")
import re 

def modify(text):
    res = ""
    pattern = re.compile(r"[A-Z][a-z]+")
    words = pattern.findall(text)
    for i, word in enumerate(words):
        if i != 0:  
            res += " " + word
        else:
            res += word
    return res
print("Lets learn some French Numbers one to five!\n")
print(modify("UnDeuxTroisQuatreCinq"))