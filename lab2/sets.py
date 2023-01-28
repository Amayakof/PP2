#1
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits: print("Yes, apple is a fruit!")
#->Yes, apple is a fruit!

#2
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
#->apple, banana, cherry, orange

#3
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)

#4
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
#->apple, cherry

#5
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
#->apple, cherry