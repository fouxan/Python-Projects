import random
import smtplib
import datetime as dt

email = "fouzanfouzan1310@gmail.com"
pw = "vixpstcdndmnnwqf"

day = dt.datetime.now().weekday()

if day == 2:
    with open("quotes.txt") as file:
        quotes = file.readlines()
        quote = random.choice(quotes)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=email, password=pw)
        connection.sendmail(from_addr=email, to_addrs=email, msg=f"Subject: Monday Motivation\n\n{quote}")
