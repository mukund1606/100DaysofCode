"""

1. Make sure you've got the correct smtp address for your email provider:

Gmail: smtp.gmail.com

Hotmail: smtp.live.com

Outlook: outlook.office365.com

Yahoo: smtp.mail.yahoo.com

"""


# How to send an email with SMTP in Python
# import smtplib

# my_email = ""
# password = ""

# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="mukund.mukulmittal@gmail.com",
#         msg="Subject:Hello\n\nThis is the body of my email.",
#     )


# import datetime as dt

# now = dt.datetime.now()
# year = now.year
# if year == 2023:
#     print("It's 2023, a new movie year!")


# date_of_birth = dt.datetime(year=1998, month=12, day=31, hour=12)
# print(date_of_birth)
