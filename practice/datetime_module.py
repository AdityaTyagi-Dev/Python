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



# Question 1: Print today's date in the format "Today is: day-month-year" (ex: Today is: 01-Jan-2027).
print("Today is:", datetime.datetime.now().strftime("%d-%b-%Y"))

# Question 2: Calculate how many days are left until New Year's Day (January 1st) from today's date.
today = datetime.date.today()
new_year = datetime.date(today.year + 1, 1, 1)
days_left = (new_year - today).days
print(f"Days left until New Year's Day: {days_left}")

# Question 3: Take a date as input from the user in DD-MM-YYYY format and print the day of the week for that date.
user_input = input("Enter a date (DD-MM-YYYY): ")
user_date = datetime.datetime.strptime(user_input, "%d-%m-%Y")
print(user_date.strftime("%A"))

# Question 4: Print the current time in 12-hour format with AM/PM
print(f"Current time: {datetime.datetime.now().strftime('%I:%M:%S %p')}")

# Question 5: Calculate a person's age in years given their birthdate as input in DD-MM-YYYY
today = datetime.datetime.today()
user_bd = input("Enter your birthday (DD-MM-YYYY): ")
user_bd_date = datetime.datetime.strptime(user_bd, "%d-%m-%Y")
age = today.year - user_bd_date.year - ((today.month, today.day) < (user_bd_date.month, user_bd_date.day))
print(age)