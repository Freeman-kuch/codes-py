#! we are writing the date in DD\MM\YYYY format
import re

dateRegex = re.compile(r'''(
                            ([0-3]?\d)
                            (/)
                            ([0-1]\d)
                            (/)
                            ([0-2]\d{3})$
                            )''', re.VERBOSE)
mo = dateRegex.search('today\'s date is 5/11/1998')  # this is where the text to be scanned will be input as strs
print(mo.group())
