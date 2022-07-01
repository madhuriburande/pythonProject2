##Exercise 1: Print current date and time in Python
from datetime import datetime
now=datetime.now()
print("Current Time:=",now)

## By using strftime format

print("Current Date is:=",now.strftime("%d-%b-%Y"))
print("Current time is:=",now.strftime("%I-%M-%S-%p"))
print()

## Exercise 2:Convert string into a datetime object
from datetime import datetime
date_string="Jun 10 2022  6:27PM"
print(date_string)
datetime_object = datetime.strptime(date_string, '%b %d %Y %I:%M%p')
print(datetime_object)
print()

##Exercise 3: Subtract a week (7 days)  from a given date in Python
from datetime import date,timedelta
given_date = date(2022, 6, 10)
print("Given Date:=",given_date)
days_to_subtract = 7
res_date=given_date-timedelta(days=days_to_subtract)
print("New_Date:=",res_date)
print()

## Exercise 4: Print a date in a the following format given_date = datetime(2020, 2, 25) exepted op=Friday 10 June 2022
from datetime import date
given_date = date(2020, 2, 25)
print("Given Dtae is:=",given_date)

print("Excepted result:=",given_date.strftime("%A %d %B %Y"))
print()

## Exercise 5: Find the day of the week of a given date
from datetime import date
given_date = date(2020, 7, 26)
print("Given date :=",given_date)
print(given_date.today().weekday())
print(given_date.strftime("%A"))
print()

## Exercise 6: Add a week (7 days) and 12 hours to a given date
from datetime import datetime,timedelta
given_date = datetime(2020, 3, 22, 10, 00, 00)
print("Given datetime=",given_date)

days_to_add=7
res_date=given_date+timedelta(days=days_to_add,hours=12)
print("Excepteded ouput:=",res_date)
print()

## Exercise 7: Print current time in milliseconds
import time
milisecond=int(round(time.time()*1000))
print("Current time in milisecond is:",milisecond)

## Exercise 8: Convert the following datetime into a string
from datetime import datetime
given_time = datetime(2020, 2, 25)
print("Given time is:=",given_time)
result=given_time.strftime("%Y-%m-%d %H-%M-%S")
print(result)

## Exercise 9: Calculate the date 4 months from the current date
#Given: 2020-02-25 ,
from datetime import datetime

from dateutil.relativedelta import relativedelta

# 2020-02-25
given_date = datetime(2020, 2, 25).date()
print("Given date is:=",given_date)

months_to_add = 4
new_date = given_date + relativedelta(months=+ months_to_add)
print("Add 4 months in curent date:=",new_date)

## Exercise 10: Calculate number of days between two given dates
#Given:
date_1 = datetime(2020, 2, 25)
print("Date 1 is:=",date_1)
date_2 = datetime(2020, 9, 17)
print("date 2 is:=",date_2)
delta=None
if date_1>date_2:
    print("Date_1 is grater")
    delta=date_1-date_2
else:
    print("Date_2 is grater ")
    delta=date_2-date_1
print("Diiference is",delta.days,"days")

