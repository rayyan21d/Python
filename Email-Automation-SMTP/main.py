import smtplib
import datetime as dt
from .env import vault # This contains a vault dictionary with email and password as keys

now = dt.datetime.now()

date_of_birth = dt.datetime(year=1999, month=2, day=9, hour=4)

test_email = vault["email"]
test_password = vault["password"]

reciever_email = vault.reciever_email
body = "Subject:Hello\n\nThis is a test email from Python."

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=test_email, password=test_password)
    connection.sendmail(
        from_addr=test_email, 
        to_addrs=reciever_email, 
        msg=body)
    print("Email sent")

