from django.core.mail import send_mail

import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os

load_dotenv()
sender = os.getenv("sender")
password = os.getenv("password")
recepient = os.getenv("recepient")


def send_daily_mail():
    service, message = set_message()
    message["Subject"] = "Daily cron message"
    message["From"] = sender
    message["To"] = recepient

    # Read the HTML file
    # try:
    #     with open("./test.html", "r") as f:
    #         html_content = f.read()
    # except Exception as e:
    #     print(f"Error reading HTML file: {e}")
    #     return False

    message.set_content("Hey there")
    # message.add_alternative(html_content, subtype='html')

    try:
        service.send_message(message)
        print("email sent")
    except Exception as e:
        print(e)
        return False
    service.quit()
    return True

def set_message():
    service = smtplib.SMTP("smtp.gmail.com", 587)
    service.starttls()
    service.login(sender, password)
    message = EmailMessage()
    return service, message
