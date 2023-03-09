# Write a Python program to subtract five days from current date.

import datetime

res = datetime.date.today()
res = res.replace(day = res.day - 5)
print(f"Today: {res}")

#result is printed in YY.MM.DD type
#reult: today 2023.03.09 -> 2023.03.04