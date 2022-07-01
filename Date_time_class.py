#Get Current Date using the Date class
from datetime import date
today=date.today()
print("Today Date is:",today)

##Get Current Time in Python
import time
t=time.time()
print(" Now Time:",t)

##Current Time Using time.ctime()
print("Current time:",time.ctime(time.time()))
print()

##Current Time Using time.localtime()

t=time.localtime(time.time())

print("Current Time:",t)
print("Current Year:",t.tm_year)
print("Current Month:",t.tm_mon)
print("Current Day:",t.tm_mday)
print()
print("Current Hour:",t.tm_hour)
print("Current Minute:",t.tm_min)
print("Current Seconds:",t.tm_sec)
print()
##Get Current Time in Milliseconds
t = time.time()
ml = int(t * 1000)
print('Current time in milliseconds:', ml)
print()

##Get Current UTC Time
from datetime import datetime,timezone
now=datetime.now(timezone.utc)
print("Current UTC Time:=",now)
