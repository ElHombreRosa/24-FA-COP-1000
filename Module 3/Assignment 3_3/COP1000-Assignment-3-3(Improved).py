# Function:     This program determines if a date entered by the user is valid.  
# Input:        Interactive
# Output:       Valid date is printed or user is alerted that an invalid date was entered.

validDate = True
MIN_YEAR = 0
MIN_MONTH = 1
MAX_MONTH = 12
MIN_DAY = 1
MAX_DAY = 31

year = None
month = None
day = None

# leap years happen ever four years 
def leap_year_feb(year):
    if (int(year) % 4 == 0 and int(year) % 100 != 0) or (int(year) % 400 == 0):
        return True 
    return False

# Get the year, then the month, then the day
# housekeeping()

month = int(input("Enter a month (numeric): "))
day = int(input("Enter a day (numeric): "))
year = int(input("Enter a year: "))

# Check to be sure date is valid

if int(year) <= MIN_YEAR: # invalid year
    validDate = False
elif int(month) < MIN_MONTH or int(month) > MAX_MONTH: # invalid month
    validDate = False
elif int(day) < MIN_DAY or int(day) > MAX_DAY: # invalid day
    validDate = False
elif int(month) in [4,6,9,11] and day > 30: # months with only 30 days 
    validDate = False
else:
    if month == 2:
        if leap_year_feb(int(year)):
            if day > 29:
                validDate = False # leap year
        else:
            if day > 28:
                validDate = False # non leap year

# Test to see if date is valid and output date and whether it is valid or not

# endOfJob()
if validDate == True:
    print(f"{month}/{day}/{year} is an valid date")
    # Output statement
else:
    print(f"{month}/{day}/{year} is an invalid date")
    # Output statement