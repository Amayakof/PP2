# Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values.
import math

a = int(input())
b = int(input())

def squares(min, max):
    n = min
    while n <= max:
        yield n ** 2
        n += 1

for i in squares(a, b):
    print(i)

