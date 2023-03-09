# Write a python program to convert snake case string to camel case string.
print("-Task 7-")
import re

def snake_ToCamel(text):
    camelCase=""
    pattern = re.compile(r"[_]")
    words=pattern.split(text)
    for i, word in enumerate(words):
        if i != 0:
            camelCase+=word.capitalize()
        else: 
            camelCase += word
    return camelCase

print(snake_ToCamel("K_B_T_U"))