#1
fruits = ["apple", "banana", "cherry"]
print(fruits[1])

#2
fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"

#3
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
#->apple, banana, cherry, orange

#4
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "lemon")
#->->apple, lemon, banana, cherry

#5
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
#->->apple, cherry

#6
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])
#->cherry

#7
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])
#->cherry, orange, kiwi

#8
fruits = ["apple", "banana", "cherry"]
print(len(fruits))
#->3