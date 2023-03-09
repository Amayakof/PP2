# Write a Python program to calculate the area of a parallelogram.
import math

base = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))

def areaParallelogram(my_base, my_height):
    return my_base * my_height

print(f"Expected Output: {areaParallelogram(base, height)}")