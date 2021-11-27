import os
import smtplib
import random
import datetime as dt
import pandas as pd

now = dt.datetime.now()

# find out which month it is
current_month = now.month

# find out which day of the month it is
current_day_of_the_month = now.day

# find out which day of the week it is
current_day_of_week = now.weekday()

# open quotes.txt file and transfer all into a list

my_email = 'kccodetest@gmail.com'
my_password = 'klayclarkecodetest'

# check to see if birthday in birthdays.csv matches today's date

df = pd.read_csv('birthdays.csv')

df.set_index('name', inplace=True)

klay_data = df.loc['Klay', :]

if klay_data['day'] == current_day_of_the_month and klay_data['month'] == current_month:
    random_letter = random.choice(os.listdir('letter_templates'))
    with open(f'letter_templates/{random_letter}') as file:
        letter = file.read().replace('[NAME]', 'Klay')
        print(letter)
    with smtplib.SMTP('smtp.gmail.com') as connection:
        # make connection secure / encrypted
        connection.starttls()
        # to login to email service
        connection.login(user=my_email, password=my_password)
        # to send mail and message
        connection.sendmail(from_addr=my_email,
                            to_addrs='klayaclarke@gmail.com',
                            msg=f'Subject:Happy Birthday\n\n{letter}')
