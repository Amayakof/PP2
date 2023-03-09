# Write a Python program to drop microseconds from datetime.

import datetime
now = datetime.datetime.now()
print (now.replace(microsecond = 0))