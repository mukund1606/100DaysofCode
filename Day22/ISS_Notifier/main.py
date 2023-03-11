import requests
from datetime import datetime
import smtplib


MY_LAT = 28.715345  # Your latitude
MY_LONG = 77.108803  # Your longitude


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = data["iss_position"]["latitude"]
    iss_longitude = data["iss_position"]["longitude"]

    if (
        MY_LAT - 5 <= float(iss_latitude) <= MY_LAT + 5
        and MY_LONG - 5 <= float(iss_longitude) <= MY_LONG + 5
    ):
        return True
    return False


def is_night_time():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True
    return False


# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user="email", password="password")
#     if is_iss_overhead() and is_night_time():
#         msg = "Subject:Look Up👆\n\nThe ISS is above you in the sky.".encode("utf-8")
#     else:
#         msg = "Subject:Look Up👆\n\nThe ISS is not above you in the sky.".encode("utf-8")

#     connection.sendmail(
#         from_addr="email",
#         to_addrs="mukund.mukulmittal@gmail.com",
#         msg=msg,
#     )

# OR

import time

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night_time():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user="email", password="password")
            msg = "Subject:Look Up👆\n\nThe ISS is above you in the sky.".encode("utf-8")
            connection.sendmail(
                from_addr="email",
                to_addrs="mukund.mukulmittal@gmail.com",
                msg=msg,
            )
