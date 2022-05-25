#! Python 3
# checks input for strength of password

import re

def strongPasswordvalidator():
    strongPasswordRegex = re.compile(r'[a-zA-Z0-9]{8,}')  # problem is it can accept all digits which is a bug
    mo1 = strongPasswordRegex.search(input('enter a password to validate\n'))
    print(f'{mo1.group() } is an Authentic Password')


while True:
    try:
        strongPasswordvalidator()
    except AttributeError:
        print('password is weak!')