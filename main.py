import smtplib

my_email = 'kccodetest@gmail.com'
my_password = 'klayclarkecodetest'

connection = smtplib.SMTP('smtp.gmail.com')

# make connection secure / encrypted
connection.starttls()
# to login to email service
connection.login(user=my_email, password=my_password)
# to send mail and message
connection.sendmail(from_addr=my_email,
                    to_addrs='klayaclarke@gmail.com',
                    msg='Subject:Code Test\n\nHello world!')
connection.close()
