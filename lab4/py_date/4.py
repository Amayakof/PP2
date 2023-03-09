# Write a Python program to calculate two date difference in seconds.

import datetime

date1 = datetime.datetime.today()
start = datetime.datetime(2005, 9, 21)
end = date1 - start
print(f"Time difference in seconds: {end.total_seconds()}")
