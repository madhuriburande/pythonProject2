##Example: Get Current DateTime in Python
from datetime import datetime
now=datetime.now()
print("Current DateTime:",now)
print("Type:",type(now))

##Extract Current Date and Time Separately from a Datetime Object
now=datetime.now()
current_date=now.date()
print("Current Date:",current_date)
current_time=now.time()
print("Current Time:",current_time)

##Break DateTime to Get Current Year, Month, Day, Hour, Minute, Seconds
now=datetime.now()
print("Current Year:",now.year)
print("Current Month:",now.month)
print("Current Day:",now.day)
print("Current Hour:",now.hour)
print("Current Minute:",now.minute)
print("Current Seconds:",now.second)
