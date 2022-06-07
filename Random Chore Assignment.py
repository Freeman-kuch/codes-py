#!python 3
# Random Chore Assignment Emailer
# this code randomly selects a chore from a list and sends the chore as a E-mail

import random, ezgmail, os, time, datetime

os.chdir('C://Users//opara//PycharmProjects')  # CWD for my credentials.json
listOfEmails = []  # This is where the E-mails to be mailed will be inputK
print('welcome to Random chore assignment')
print('Generating chores')


def emailChore():
    for idx, Emails in enumerate(listOfEmails):
        chores = ['reformatting files', 'front-end JavaScript', 'Backend development', 'cooking', 'Driving',
                  'Robotics process automation']
        randomChore = random.choice(chores)
        ezgmail.send(listOfEmails[idx], 'Your Chore has been Generated',
                     f'{time.ctime()}\n\nDear Reader, \n\nYour chore has been selected at Random.\n\nyour chore is "{randomChore}".\n\nPlease Go right ahead and begin your Chore! \n\nkind Regards,\nFreeman :).')
        chores.remove(randomChore)
        print(f'sending chore to {Emails} ...')
        time.sleep(1)
        print('sent')
        time.sleep(0.5)


def weeklyLoop():
    timeFrame = datetime.timedelta(weeks=1, days=0, hours=0, minutes=0, seconds=0)  # this helps define the 1week timer
    secondstimeFrame = timeFrame.total_seconds()  # converts to seconds
    while secondstimeFrame > 0:
        time.sleep(1)
        secondstimeFrame = secondstimeFrame - 1


while True:
    ezgmail.init()
    emailChore()
    print(f'Chores Distribution Done on {str(datetime.datetime.now())}')
    weeklyLoop()
