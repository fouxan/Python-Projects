import smtplib

my_email = "fouzanfouzan1310@gmail.com"
pw = "vixpstcdndmnnwqf"

connection = smtplib.SMTP("smtp.gmail.com", port=587)
connection.starttls()
connection.login(user=my_email, password=pw)
connection.sendmail(from_addr=my_email, to_addrs="fouxann1310@gmail.com",
                    msg="Subject: Trial mail\n\n This is a trial mail.")
connection.close()