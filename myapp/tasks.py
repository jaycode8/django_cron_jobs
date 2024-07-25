from django.core.mail import send_mail

import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os

load_dotenv()
sender = os.getenv("sender")
password = os.getenv("password")


def send_daily_mail():
    service, message = set_message()
    message["Subject"] = "Daily cron message"
    message["From"] = sender
    message["To"] = "jamesmumo443@gmail.com"
    message.set_content("Hey this is your daily email message")
    try:
        service.send_message(message)
    except Exception as e:
        return False
    service.quit()
    return True

def set_message():
    service = smtplib.SMTP("smtp.gmail.com", 587)
    service.starttls()
    service.login(sender, password)
    message = EmailMessage()
    return service, message
