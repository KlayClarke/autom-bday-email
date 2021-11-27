import smtplib
import random
import datetime as dt

# find out which day of the week it is

now = dt.datetime.now()
current_day_of_week = now.weekday()

# open quotes.txt file and transfer all into a list

my_email = 'kccodetest@gmail.com'
my_password = 'klayclarkecodetest'

if current_day_of_week == 0:
    with open('quotes.txt', mode='r') as file:
        list_of_quotes = file.readlines()

    random_quote = random.choice(list_of_quotes)

    with smtplib.SMTP('smtp.gmail.com') as connection:
        # make connection secure / encrypted
        connection.starttls()
        # to login to email service
        connection.login(user=my_email, password=my_password)
        # to send mail and message
        connection.sendmail(from_addr=my_email,
                            to_addrs='klayaclarke@gmail.com',
                            msg=f'Subject:Quote Of The Day\n\n{random_quote}')
