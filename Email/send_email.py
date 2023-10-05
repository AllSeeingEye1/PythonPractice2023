import smtplib
import ssl
import email.message 
from email.message import EmailMessage

subject = "Email From Python"

body = "This is a test email from Python!"
sender_email = input("Input your G-Mail: ")
receiver_email = input("Input recipients G-Mail: ")
password = ("Enter a password: ")

message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.set_content(body)

context = ssl.create_default_context()

print("Sending email")
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())

print("Success!")