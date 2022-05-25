#! Python 3
# Date Validation with regular expressions
# we are writing regular expressions to detect the date in DD\MM\YYYY format from clipboard
import re, pyperclip

dateRegex = re.compile(r'''(
                            [0-3]?\d                
                            [/,.-]
                            [0-1]?\d              
                            [/,.-]
                            [1-2]\d{3}            
                            )''', re.VERBOSE)
mo = dateRegex.findall(pyperclip.paste())  # this is where the date(s) copied to clipboard to be scanned will be input as strs
# TODO : solve problem of single digits day and month, and double digit year
# these variables assigned are for DD, MM,  YY and are also converted to integer
day = 0
month = 0
year = 0
print('Starting Date Validation ...')
for i, d in enumerate(mo):
    day = int(mo[i][:2])
    month = int(mo[i][3:5])
    year = int(mo[i][6:])
    leapYearCheck = year % 4 == 0    # Leap years are every year evenly divisible by 4
    # date validation
    if day > 31:
        print(f'This Date{mo[i]} in incorrect')
        continue
    elif day == 31:
        if month == 4 or month == 6 or month == 9 or month == 11:
            print(f'This month in {mo[i]} has 30-Days Only.')
            continue
        elif month == 2:
            print(f'This month in {mo[i]} has 28-Days Only unless this is a Leap-year which it has 29-Days.')
            continue
    elif day == 29:
        if month == 2:
            if not leapYearCheck:
                print(f'This month in {mo[i]} can\'t have 29-Days, it\'s not a leap year.')
                continue
    elif month > 12:
        print(f'This month in {mo[i]} isn\'t valid(a year can have only 12Months).')
        continue
    print(f'{mo[i]} is a valid Date.')

print('\nDate Validation Done :)')