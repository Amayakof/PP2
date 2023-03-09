# Write a Python program to subtract five days from current date.

import datetime

my_day = datetime.date.today()
print(f"Today: {my_day}")
my_day= my_day.replace(day = my_day.day - 5)
print(f"Five days ago: {my_day}")

#result is printed in YY.MM.DD type
#reult: today 2023.03.09 -> 2023.03.04