# Write a Python program to print yesterday, today, tomorrow.

import datetime

today = datetime.date.today()
yesterday = today.replace(day = today.day - 1)
tomorrow = today.replace(day = today.day + 1)
print( )
print(f" Yesterday: {yesterday}\n", f"Today: {today}\n", f"Tomorrow: {tomorrow}")
