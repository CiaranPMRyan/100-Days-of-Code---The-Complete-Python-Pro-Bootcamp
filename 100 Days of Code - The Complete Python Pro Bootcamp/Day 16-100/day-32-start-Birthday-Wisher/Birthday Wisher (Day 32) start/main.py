# import smtplib
#
# my_email = "appbreweryciarantest@gmail.com"
# password = "vpkvfnlaqezctbky"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()#
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs="appbreweryciarantest@yahoo.com", msg="Subject:Hello world!\n\nHere is my text")
#     connection.close()



import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()

date_of_birth = dt.datetime(year=1980, month=12, day=22)
print(date_of_birth)