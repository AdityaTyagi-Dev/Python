# Importing the module
import datetime

# Getting today's date [Method 1]
today = datetime.date.today()
print(today)

# Getting today's date [Method 2]
tday = datetime.datetime.now().date()
print(tday)

# Creating a custom date
d = datetime.date(2025, 12, 25)
print(d)

# Accessing year, month, day
print(d.day)
print(d.month)
print(d.year)

# Getting current time
curTime = datetime.datetime.now().time()
print(curTime)

# Creating a custom time
t = datetime.time(12, 0, 0)
print(t)

# Accessing hour, minute, second
print(t.hour)
print(t.minute)
print(t.second)

# Getting current datetime

curDT = datetime.datetime.now()
print(curDT)

# Creating custom datetime
dt = datetime.datetime(2025, 12, 25, 12, 0) #(year, month, day, hour, minute, second)
print(dt)

# Formatting dates and times
now = datetime.datetime.now()
print(now.strftime("%d-%m-%Y"))

"""
%d - date [DD]
%m - month [MM]
%y - year [YY]
%Y - year [YYYY]
%D - date [DD/MM/YY]
%H - hour [HH][24 hour]
%M - minute [MM]
%S - second [SS]
%A - day [complete]
%a - day [only first three char]
%B - month [complete]
%b - month [only first three char]
%I - hour [HH][12 hour]
%p - am/pm
"""

# String to datetime
text = "01-01-2027"
textToDate = datetime.datetime.strptime(text, "%d-%m-%Y")
print(textToDate)

# timedelta
future = now + datetime.timedelta(days=7)
print(future)