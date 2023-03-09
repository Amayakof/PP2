# Write a Python program to calculate the area of regular polygon.
import math

apothem = float(input("Length of the Apothem: "))
numside = int(input("Number of Sides: "))
length = float(input("Length of a Side: "))

def polygonArea(my_apothem, my_length, my_numside):
    return (my_apothem * my_length * my_numside)/2

print(f"The area of The Polygon is: {polygonArea(apothem, length, numside)}")

