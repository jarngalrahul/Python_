import email
import imaplib
from email.message import EmailMessage
import os
import smtplib

GOOGLE_TEST_MAIL = os.environ.get("GOOGLE_TEST_MAIL")
GOOGLE_TEST_PASSWORD = os.environ.get("GOOGLE_TEST_PASSWORD")
imap_url = 'imap.gmail.com'
you = 'testingpython63@yahoo.com'

textfile = "SendReadMails/textfile.txt"

# ---------------------------------- Sending an email----------------------------#
with open(textfile) as fp:
    msg = EmailMessage()
    msg.set_content(fp.read())

msg['Subject'] = f'The contents of a textfile'
msg['From'] = GOOGLE_TEST_MAIL
msg['To'] = you

s = smtplib.SMTP(host='smtp.gmail.com', port=587)
s.starttls()
s.login(user=GOOGLE_TEST_MAIL, password=GOOGLE_TEST_PASSWORD)
s.send_message(msg=msg)
s.quit()

# ---------------------------------- Reading an email-------------------------------#
# Importing libraries

# this is done to make SSL connection with GMAIL -> logging the user in
con = imaplib.IMAP4_SSL(host=imap_url, port=993)
con.login(GOOGLE_TEST_MAIL, GOOGLE_TEST_PASSWORD)
con.select('inbox')

mail_ids = []
status, data = con.search(None, 'ALL')  # Searches all emails in inbox
print(status)  # OK
print(data)  # gives us a byte string [b'1 2 3 4 5 6 7 8 9 10 11']
for block in data:
    print(block)
    mail_ids += block.split()
print(mail_ids)

for id in mail_ids:
    status, data = con.fetch(id, '(RFC822)')
    # print(data)
    for response_part in data:
        # if the data is a tuple ignore 0 and 2 response is in 1 index
        if isinstance(response_part, tuple):
            message = email.message_from_bytes(response_part[1])
            mail_from = message['from']
            mail_sub = message['subject']
            if message.is_multipart():
                mail_content = ''
                for part in message.get_payload():
                    if part.get_content_type() == 'text/plain':
                        mail_content += part.get_payload()
            else:
                mail_content = message.get_payload()
            print(f'From: {mail_from}')
            print(f'Subject: {mail_sub}')
            print(f'Content: {mail_content}')
