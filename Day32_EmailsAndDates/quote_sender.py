from random import choice
import datetime as dt
import smtplib


my_email = "pythontesting1922@gmail.com"
password = "pcclpkpetjtlyxqd"
sending_addr = "testingpython63@yahoo.com"

# mails should be sent on this days
current_weekday_day = dt.datetime.now().weekday()

if current_weekday_day == 1:
    with open(file="Day32_EmailsAndDates//quotes.txt", mode="r") as quote_data:
        quotes = quote_data.readlines()
        quote_sent = choice(quotes)
        print(quote_sent)

    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=sending_addr,
                            msg=f"Subject:Quote of the day....\n\n{quote_sent}"
                            )
