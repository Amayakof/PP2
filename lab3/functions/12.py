# 12
# Define a function histogram() that takes a list of integers and prints a histogram to the screen. 

print("!!!TASK 12!!!")
def histogram(values):
    star = '*'
    for value in values:
        if value != 0:
            star = star * value
        else:
            star = ''
        print(star)
        star = '*'

histogram ([1, 0, 2, 0, 3])