import os
import smtplib

MY_EMAIL = os.environ.get("GOOGLE_TEST_MAIL")
PASSWORD = os.environ.get("GOOGLE_TEST_PASSWORD")


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def send_mails(self, names, emails, message):
        with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            for num in range(len(emails)):
                print(f"Emailing {names[num]}")
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=emails[num],
                    msg=f"Subject:New Low Price Flight!\n\nHi {names[num]}\n{message}"
                )
