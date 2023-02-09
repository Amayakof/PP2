
import math

#6
# Write a function that accepts string from user, return a sentence with the words reversed. 
# We are ready -> ready are We
print("!!!TASK 6!!!")
def rev_string(sentence):
    words = sentence.split()
    words.reverse()
    print(''.join(words))

s = input()
rev_string(s)
