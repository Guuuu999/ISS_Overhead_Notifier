import requests
from datetime import datetime
from smtplib import *
import time

MY_LAT = 40.712776 # Your latitude
MY_LONG = -74.005974 # Your longitude

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    print(iss_latitude, iss_longitude)

    if MY_LAT - 5 < iss_latitude < MY_LAT + 5 and MY_LONG - 5 < iss_longitude < MY_LONG + 5:
        return True

def is_night():
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
    print(sunrise, sunset)

    time_now = datetime.now()
    hour = time_now.hour

    if hour >= sunset or hour <= sunrise:
        return True

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
            my_email = "myemail"
            pwd = "mypassword"
            # create the object and specify the location of our email provider's SMTP server
            with SMTP("smtp.gmail.com") as connection:
                # this line is to secure the email transportation, so it's encrypted
                connection.starttls()
                connection.login(user=my_email, password=pwd)
                connection.sendmail(from_addr=my_email, to_addrs="erinhope999@yahoo.com",
                                        msg=f"Subject: Look Up\n\nLook up!")




