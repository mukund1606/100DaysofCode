##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

import pandas as pd
import datetime as dt
import random
import smtplib

today = dt.datetime.now()
today_tuple = (today.month, today.day)
data = pd.read_csv("birthdays.csv")

birthdays_dict = {
    (data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()
}


if today_tuple in birthdays_dict:
    # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
    birthday_person = birthdays_dict[today_tuple]
    letter = random.randint(1, 3)
    file_path = f"letter_templates/letter_{letter}.txt"
    with open(file_path) as letter:
        contents = letter.read()
        contents = contents.replace("[NAME]", birthday_person["name"])
    # 4. Send the letter generated in step 3 to that person's email address.
    email = ""
    password = ""
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(
            from_addr=email,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}",
        )
