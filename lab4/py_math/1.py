
# Write a Python program to convert degree to radian.
import math

degree = float(input("Input degree: "))

def DegToRad(degree):
    return degree / 180 * math.pi

print(f"Radian value: {DegToRad(degree)}")
