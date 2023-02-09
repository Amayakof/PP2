import math

#1
# A recipe you are reading states how many grams you need for the ingredient. 
# Unfortunately, your store only sells items in ounces. 
# Create a function to convert grams to ounces. ounces = 28.3495231 * grams
print("TASK 1")

print("Translate ounces to grams :)")
print("Please, enter the value(oz): ")
grams = float(input())

def g_to_oz(grams):
    oz = 28.3495231 * grams
    print("Values in oz:", oz)

g_to_oz(grams)
