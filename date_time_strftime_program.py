##Python DateTime Format Using Strftime()
##How to Format Date and Time in Python
##que.Example: Convert DateTime to String Format

from datetime import datetime
now=datetime.now()

date_time_str=now.strftime("%y-%m-%d-%H-%M-%S")
print("Dtae Time In String:",date_time_str)

## 2 da way
now=datetime.now()

Date=now.strftime("%y/%m/%d")
print("Current Date is:=",Date)
print()

Time=now.strftime("%H/%M/%S")
print("Current Time is:=",Time)

Year=now.strftime("%y")
print("Year:=",Year)

Month=now.strftime("%m")
print("Month:=",Month)

Day=now.strftime("%d")
print("Day:=",Day)

## Represent Dates in Textual Format
x_date=datetime.now()
print("Curent DateTime:=",x_date)
print()

print("dd-Monthname-YY:=",x_date.strftime("%d-%B-%Y"))
print()
## Represent Dates in full  Textual Format
print("Dayname-dd-Monthname-yy:=",x_date.strftime("%A,%d-%B-%Y"))
## Represent Dates in short  Textual Format
print("dayname-dd-monthname-yy:=",x_date.strftime("%a,%d-%b-%y"))

##Convert Only Date to String
from datetime import date
now=datetime.now()
print("Today's date:=",now)

## in sttring format
print("Today's date:=",now.strftime("%d-%m-%y"))

## Convert Time Object to String Format
x_time=datetime.now()
print("Current Time:=",x_time)
print()

##Use the %H-%M-%S format code to display time in 24-hours format
print("Time in 24 hours format:=",x_time.strftime("%H-%M-%S"))

print("Time in 12 hours format:=",x_time.strftime("%I-%M-%S"))
print()

## Represent Time in Microseconds Format
x_time = datetime.now().time()
print('Current Time:', x_time)

# Represent time in Microseconds (HH:MM:SS.Microsecond)
print("Time is:", x_time.strftime("%H:%M:%S.%f"))
print()

## Represent Time in AM/PM Format Use the %p format code to represent time in AM/PM format.
now=datetime.now()
print("Current datetime",now)
print()

print("Time is 24 hour format:=",now.strftime("%H-%M-%S-%p"))
print("Time is 12 hours format:=",now.strftime("%I-%M-%S-%p"))


