import smtplib
import datetime as dt

# my_email = 'kccodetest@gmail.com'
# my_password = 'klayclarkecodetest'
#
# with smtplib.SMTP('smtp.gmail.com') as connection:
#     # make connection secure / encrypted
#     connection.starttls()
#     # to login to email service
#     connection.login(user=my_email, password=my_password)
#     # to send mail and message
#     connection.sendmail(from_addr=my_email,
#                         to_addrs='klayaclarke@gmail.com',
#                         msg='Subject:Code Test\n\nHello world!')
now = dt.datetime.now()
current_day_of_week = now.weekday()
print(current_day_of_week)