#!python 3
# Random Chore Assignment Emailer
# this code randomly selects a chore from a list and sends the chore as a E-mail

import random, ezgmail, os

os.chdir('C://Users//opara//PycharmProjects')
listOfEmails = ['freemanoparaocha@gmail.com', 'newmanchidike@yahoo.com', 'prochess91@gmail.com', 'mglory360@ymail.com']
chores = ['reformatting files', 'front-end JavaScript', 'cleaning', 'cooking', 'Driving']
randomChore = random.choice(chores)

print('welcome to Random chore assignment')
print('Generating chores ...')

ezgmail.init()
