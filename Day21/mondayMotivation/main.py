import datetime as dt
import smtplib
import random

my_email = ""
password = ""

now = dt.datetime.now()
current_day = now.weekday()
if current_day == 5:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="mukund.mukulmittal@gmail.com",
            msg=f"Subject:Motivation\n\n{quote}",
        )
