# Write a Python program to calculate two date difference in seconds.

import datetime

fin = datetime.datetime.today()
start = datetime.datetime(2005, 9, 21)
end = fin - start
print(f"Standard output: {end}\n")
print(f"Time difference in seconds: {end.total_seconds()}")
