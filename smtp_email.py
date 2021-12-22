# #!/usr/bin/python

# import smtplib
# import base64

# filename = "/tmp/test.txt"

# # Read a file and encode it into base64 format
# fo = open(filename, "rb")
# filecontent = fo.read()
# encodedcontent = base64.b64encode(filecontent)  # base64

# sender = 'webmaster@tutorialpoint.com'
# reciever = 'amrood.admin@gmail.com'

# marker = "AUNIQUEMARKER"

# body ="""
# This is a test email to send an attachement.
# """
# # Define the main headers.
# part1 = """From: From Person <me@fromdomain.net>
# To: To Person <amrood.admin@gmail.com>
# Subject: Sending Attachement
# MIME-Version: 1.0
# Content-Type: multipart/mixed; boundary=%s
# --%s
# """ % (marker, marker)

# # Define the message action
# part2 = """Content-Type: text/plain
# Content-Transfer-Encoding:8bit

# %s
# --%s
# """ % (body,marker)

# # Define the attachment section
# part3 = """Content-Type: multipart/mixed; name=\"%s\"
# Content-Transfer-Encoding:base64
# Content-Disposition: attachment; filename=%s

# %s
# --%s--
# """ %(filename, filename, encodedcontent, marker)
# message = part1 + part2 + part3

# try:
#    smtpObj = smtplib.SMTP('localhost')
#    smtpObj.sendmail(sender, reciever, message)
#    print( "Successfully sent email")
# except Exception:
#    print( "Error: unable to send email")

import mimetypes
import os 
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.mime.base import MIMEBase


port = 465  # Connect to SSL port 
smtp_server = "smtp.gmail.com"

subject = "An email With An Affirmation Attached...Again"
body = "Here's an affirmation sent with Python"
sender_email =  os.environ['EMAIL_USER']
receiver_email = f"queenscriptqueen@gmail.com"
password = os.environ['EMAIL_PASSWORD']
# To send multipart message and set headers
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message["Bcc"] = receiver_email 

# Use attach method and format body string to plain text for email body
message.attach(MIMEText(body, "plain"))

filename = "QUEENSFORM_ENOUGH.jpg"  # In same directory as script

""""" 
Add to with open() as syntax to have dynamic MIMEBase variables 
with import of mimtypes 
"""


# Open file in binary mode
with open(filename, "rb") as attachment:
    # Add file as application/octet-stream
    # Email client can usually download this automatically as attachment
    part = MIMEBase("application", "image/jpeg")
    part.set_payload(attachment.read())

# Encode file in ASCII characters to send by email    
encoders.encode_base64(part)

# Add header as key/value pair to attachment part
part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)

# Add attachment to message and convert message to string
message.attach(part)
text = message.as_string()

# Log in to server using secure context and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, text)
# Create a secure SSL context
context = ssl.create_default_context()

# Try to log in to server and send email
try:
    server = smtplib.SMTP(smtp_server,port)
    server.ehlo() # Can be omitted
    server.starttls(context=context) # Secure the connection
    server.ehlo() # Can be omitted
    server.login(sender_email, password)
    # TODO: Send email here
except Exception as e:
    # Print any error messages to stdout
    print(e)
finally:
    server.quit() 





# with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
#     server.login("my@gmail.com", password)
    # TODO: Send email here