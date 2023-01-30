#1
x = input("Enter value: ") 
cnt = 0 
y = set("aeiou") 
for letter in x: 
    if letter in y: 
        cnt += 1 
print("Vowels: ") 
print(cnt)

#2
x = int(input())
x_copy = x
y = 0
t = 0

while(x>0):
   t = x % 10
   y = y * 10 + t
   x = x // 10
if x_copy == y:
    print("yes")
    
else:
    print("no")

#3
x = str(input())
mySet = set(x)
for bukva in mySet:
    kolichestvo = 0
    for character in x:
        if character == bukva:
            kolichestvo += 1
    print(" {} -> {}".format(bukva, kolichestvo))