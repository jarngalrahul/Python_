##################### Extra Hard Starting Project ######################

# TODO:1. Update the birthdays.csv

# TODO:2. Check if today matches a birthday in the birthdays.csv

# TODO:3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# TODO:4. Send the letter generated in step 3 to that person's email address.


import datetime as dt
import random
import smtplib
import pandas

current_datetime = dt.datetime.now()
cur_day = current_datetime.day
cur_month = current_datetime.month
MY_EMAIL = "pythontesting1922@gmail.com"
PASSWORD = "*****************"
MAILING_ADDR = "testingpython63@yahoo.com"


def mail_text(person):
    letter_choice = random.randint(1, 3)
    with open(file=f"Day32_EmailsAndDates/Birthday Wisher/letter_templates/letter_{letter_choice}.txt", mode="r") as file:
        data = file.readlines()
        data[0] = data[0].replace("[NAME]", person['name'])
        mail_text = "Subject:Birthday Wishes\n\n"+"".join(data)
        return mail_text


def send_birthday_mail(person):
    birthday_message = mail_text(person)
    print(birthday_message)
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=person['email'],
                            msg=birthday_message)


def birthday_wisher():
    data = pandas.read_csv(
        filepath_or_buffer="Day32_EmailsAndDates/Birthday Wisher/birthdays.csv")
    persons = data.to_dict(orient="records")
    for person in persons:
        if person['month'] == cur_month and person['day'] == cur_day:
            send_birthday_mail(person)


birthday_wisher()
