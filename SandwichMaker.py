#! Python 3
# Sandwich Maker
# this code acts Like a restaurant sandwich menu which prompts users for their preference on sandwich


import pyinputplus as pyip

totalCost = 0

print('what are your preference for your burger?')
BreadType = pyip.inputMenu(['wheat', 'white', 'sourdough'])
if BreadType == 'wheat':
    totalCost = totalCost + 2
elif BreadType == 'white':
    totalCost = totalCost + 3
else:
    totalCost = totalCost + 5

proteinType = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'])
if proteinType == 'chicken':
    totalCost = totalCost + 2
elif proteinType == 'turkey':
    totalCost = totalCost + 5
elif proteinType == 'ham':
    totalCost = totalCost + 1.5
else:
    totalCost = totalCost + 1

print('would you like to have cheese? Yes/No')
cheese = pyip.inputYesNo()
if cheese == 'yes':
    cheeseType = pyip.inputMenu(['cheddar', 'Swiss', 'mozzarella'])
    if cheeseType == 'cheddar':
        totalCost = totalCost + 1
    elif cheeseType == 'Swiss':
        totalCost = totalCost + 1
    else:
        totalCost = totalCost + 1
else:
    totalCost = totalCost

print('what do you want anything added?')
more = pyip.inputYesNo('yes or no\n')
if more == 'yes':
    print('which do you want?')
    extra = pyip.inputMenu(['mayo', 'mustard', 'lettuce', 'tomato'])
    if extra == 'mayo':
        totalCost = totalCost + 1
    elif extra == 'mustard':
        totalCost = totalCost + 1
    elif extra == 'lettuce':
        totalCost = totalCost + 1
    else:
        totalCost = totalCost + 1
else:
    print('ok!')

print('how many Burgers do you want?')
numberOfBurgers = pyip.inputInt(min=1)

print(f'okay! your order has been taken and the bill is: \n ${totalCost *numberOfBurgers}')







