##################### Extra Hard Starting Project ######################

import datetime as dt
from operator import index

import pandas as pd
import random
import smtplib


# 1. Update the birthdays.csv
# Done. I just manually wrote in the items

# 2. Check if today matches a birthday in the birthdays.csv
today = dt.datetime.today()
today_tuple = (today.month, today.day)

birthday_list = pd.read_csv("birthdays.csv", encoding="utf-8")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in birthday_list.iterrows()}
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

    letter_list = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
    letter = random.choice(letter_list)

    with open(f"./letter_templates/{letter}", "r") as letter:
        body = letter.read()
        new_letter = body.replace("[NAME]", birthday_person["name"])

# 4. Send the letter generated in step 3 to that person's email address.

    my_email = "appbreweryciarantest@gmail.com"
    password = "vpkvfnlaqezctbky"
    message = new_letter

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="ciaran@burgschneider.com", msg=f"Subject:Happy birthday!\n\n{message}")
        connection.close()
