
# call-able reusable function to send email

import smtplib                                                  #loads smtplib internal library
from email.message import EmailMessage                          #get contents of email message
import os                                                       #lets python access other ??

def send_email(sender, receivers, subject, body):
    app_password = "################"     #replace with real password
    print("Test sender =", sender)
    #app_password = os.getenv ("EMAIL_APP_PASSWORD")

    #if not app_password:
        #raise ValueError ("EMAIL_APP_PASSWORD not set")

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = ",".join(receivers)
    msg.set_content(body)



    with smtplib.SMTP("smtp.gmail.com", 587) as server:     #connect to gmail server
        server.starttls()                                   #turn on encryption
        server.login(sender, app_password)                  #login to gmail
        server.send_message(msg)                            #sends the email with "msg"
    print("Email sent successfully!")

