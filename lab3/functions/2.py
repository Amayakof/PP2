import math

#2
# Read in a Fahrenheit temperature. 
# Calculate and display the equivalent centigrade temperature. 
# The following formula is used for the conversion: C = (5 / 9) * (F – 32)
print("TASK 2")

print("Translate Farenheit to Celcius :)")
print("Please, enter the value(Fº): ")
F = float(input())

def f_to_c(F):
    C = (5 / 9) * (F - 32)
    print("Values in Cº:", C)

f_to_c(F)
