import math

#3
# Write a program to solve a classic puzzle:
# We count 35 heads and 94 legs among the chickens and rabbits in a farm. 
# How many rabbits and how many chickens do we have? create function: solve(numheads, numlegs):
print("TASK 3")

def solve(numheads, numlegs):
    num_chicken = 0
    num_rabbits = 0
    for i in range(1, numheads + 1):
        num_chicken = i
        num_rabbits = numheads - i
        if(num_chicken * 2 + num_rabbits * 4 == numlegs):
            break
    print(f"Rabbits: {num_rabbits} Chicken: {num_chicken}")

solve(35, 94)
