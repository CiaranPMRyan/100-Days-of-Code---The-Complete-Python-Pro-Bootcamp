import smtplib
import datetime as dt
import random

def getMessage():
    with open('quotes.txt', 'r') as file:
        quote = file.readlines()
    message = random.choice(quote)
    return message

def sendMail():
    my_email = "appbreweryciarantest@gmail.com"
    password = "vpkvfnlaqezctbky"
    message = getMessage()

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        #connection.set_debuglevel(1)
        connection.ehlo()
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="ciaran@burgschneider.com", msg=f"Subject:Morning Quote!\n\n{message}")
        connection.close()

def main():
    now = dt.datetime.now()
    day_of_week = now.weekday()
    if day_of_week == 1:
        sendMail()

main()