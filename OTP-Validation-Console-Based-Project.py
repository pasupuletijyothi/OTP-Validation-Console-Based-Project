import smtplib
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
n = ["paramjyothipasupuleti123@gmail.com","tejaswiemani1010@gmail.com","rokkalasailaja01@gmail.com","pujaparchuri@gmail.com"]
for i in n:
    
    

    otp = random.randint(1111,9999)
    body = f"OTP for Verification is {otp}"

    msg = MIMEMultipart()
    msg["From"] = "paramjyothipasupuleti123@gmail.com"
    msg["To"] = i
    msg["Subject"] = "OTP For Validation"
    msg.attach(MIMEText(body,'plain'))


    server = smtplib.SMTP("Smtp.gmail.com",587)
    server.starttls()
    server.login("paramjyothipasupuleti123@gmail.com","vefp tkpf rfwt rqun")
    server.send_message(msg)
    server.quit()

    cotp = int(input("Enter OTP Recieved: "))
    if otp == cotp:
        print("OTP Verification Success")
    else:
        print("Invalid OTP")
















































