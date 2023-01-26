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