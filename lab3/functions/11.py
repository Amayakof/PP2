# 11
# Write a Python function that checks whether a word or phrase is palindrome or not. 
# Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam
print("!!!TASK 11!!!")
def is_palindrome(s):
    char_list = [s[i] for i in range(len(s))]
    char_list.reverse()
    s1 = ''.join(char_list)
    return s == s1
