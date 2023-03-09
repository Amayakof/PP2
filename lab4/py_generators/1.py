# Create a generator that generates the squares of numbers up to some number N.
import math

n = int(input())

def square_gen(max):
    n = 1
    while n <= max:
        yield n ** 2
        n += 1
        

for i in square_gen(n):
    print(i)
