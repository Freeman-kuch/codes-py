#! Python 3
# Date Validation with regular expressions
# we are writing regular expressions to detect the date in DD\MM\YYYY format
import re

dateRegex = re.compile(r'''(
                            [0-3]?\d                
                            [/]
                            [0-1]?\d              
                            [/]
                            [1-2]\d{3}            
                            )''', re.VERBOSE)
mo = dateRegex.findall('today\'s date is 29/02/2001 and 28/13/2017')  # this is where the text to be scanned will be input as strs
# TODO : solve problem of single digits day and month, and double digit year
# these variables assigned are for DD, MM,  YY and are also converted to integer
day = 0
month = 0
year = 0
for i, d in enumerate(mo):
    day = int(mo[i][:2])
    month = int(mo[i][3:5])
    year = int(mo[i][6:])
    leapYearCheck = year % 4 == 0    # Leap years are every year evenly divisible by 4
    # print(f'{day} {month} {year}')
    # print(mo)
    # date validation
    if day > 31:
        raise 'This Date in incorrect'
        continue
    elif day == 31:
        if month == 4 or month == 6 or month == 9 or month == 11:
            raise 'This month has 30-Days Only'
        elif month == 2:
            raise 'This month has 28-Days Only unless this is a Leap-year which it has 29-Days'
    elif day == 29:
        if month == 2:
            if not leapYearCheck:
                print('This month can\'t have 29-Days, it\'s not a leap year')
        continue
