
# Write a Python program to calculate the area of a trapezoid.
import math

h = float(input("Height: "))
a = float(input("Base_1: "))
b = float(input("Base_2: "))

def TrapezoidArea(height, baseA, baseB):
    return (baseA + baseB) / 2 * height

print(f"The area of Trapezoid: {TrapezoidArea(h, a, b)}")