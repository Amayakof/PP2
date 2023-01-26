#1
x = input("Enter value: ") 
cnt = 0 
y = set("aeiou") 
for letter in x: 
    if letter in y: 
        cnt += 1 
print("Vowels: ") 
print(cnt)