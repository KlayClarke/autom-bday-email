import os
import smtplib
import random
import datetime as dt
import pandas as pd

now = dt.datetime.now()

# find out which month it is
current_month = now.month

# find out which day of the month it is
current_day = now.day

# find out which day of the week it is
current_day_of_week = now.weekday()

today = (current_month, current_day)

# open quotes.txt file and transfer all into a list

my_email = 'kccodetest@gmail.com'
my_password = 'klayclarkecodetest'

# check to see if birthday in birthdays.csv matches today's date

# create data frame from csv

df = pd.read_csv('birthdays.csv')

# create dictionary from data frame using dict comprehension

birthdays_dict = {(row.month, row.day): row for (index, row) in df.iterrows()}

# if today's date is present in birthdays_dict (means that someone's birthday is today) - send person a birthday email

if today in birthdays_dict:
    birthday_name = birthdays_dict[today]['name']
    birthday_email = birthdays_dict[today]['email']
    random_letter = random.choice(os.listdir('letter_templates'))
    with open(f'letter_templates/{random_letter}') as file:
        letter = file.read().replace('[NAME]', birthday_name)
        print(letter)
    with smtplib.SMTP('smtp.gmail.com') as connection:
        # make connection secure / encrypted
        connection.starttls()
        # to login to email service
        connection.login(user=my_email, password=my_password)
        # to send mail and message
        connection.sendmail(from_addr=my_email,
                            to_addrs=birthday_email,
                            msg=f'Subject:Happy Birthday\n\n{letter}')
