import smtplib

test_email = ""
test_password = " "

reciever_email = " "
body = "Subject:Hello\n\nThis is a test email from Python."

connection = smtplib.SMTP("smtp.gmail.com", port=587)
connection.starttls()
connection.login(user=test_email, password=test_password)
connection.sendmail(from_addr=test_email, to_addrs=reciever_email, msg=body)

connection.close()