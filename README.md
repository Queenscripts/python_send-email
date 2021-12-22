# Sending Emails With Python

!["Email Image"](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSsCi2BOTyBN5Mbx7S2szLdKToz_SrpiHmq0Q&usqp=CAU)

### Why is this topic important? 

Email is one of the most cost-effective and tried-and-true way of staying connected with users. For generating notifications and sharing alerts, email is extremely beneficial due to accessibility. 

#### There are three ways to send emails with Python. 

### SMTP 
##### SMTP PROTOCOL CLIENT 
Built into Python, this module defines SMTP Simple Mail Transfer Protocol. It uses the RFC 821 protocol for SMTP. Paired with IMAP (Internet Message Access Protocol- used by email clients to retrieve email messages from a mail server over an internet protocol suite Transmission Control Protocol/Internet Protocol - TCP/IP - connection) or POP3 ( Post Office Protocol - a one-way client-serer protocol in which email is received and held on the email server where a recipient or email client can download mail periodically from the server).

##### EMAIL AND MIME HANDLING PACKAGE


### Transactional Email Service 
Sending automated or large volume emails are integral for mass communication. For viewing statistics on emails, reliable delivery, and support, transactional email services is agood option. Services like Sengrid  

### Multichannel Notifications Service 

## Setup

### Installation

Set up virtualenv - a Python tool that helps manage dependencies, install requirements: 

```
1.  virtualenv env 
2.  source env/bin/activate 
3.  pip install -r requirements.txt
4.  source secrets.sh
```

### Run the application
```
python flask_email.py
python smtp_email.pys
```
Navigate to http://localhost:5000. 


#### Appendix


##### RESOURCES 

1. [Email and MIME Handling Package](https://docs.python.org/3/library/email.html)
2. [POP3 Protocol Client](https://docs.python.org/3/library/poplib.html#module-poplib)
3. [Internet Data Handling](https://docs.python.org/3/library/netdata.html)
4. [Unicdoe & Email](https://en.wikipedia.org/wiki/Unicode_and_email)
5. [Email](https://en.wikipedia.org/wiki/Email)
6. [EmaSend Email programmatically with Gmail, Python, and Flaskil](https://www.twilio.com/blog/2018/03/send-email-programmatically-with-gmail-python-and-flask.html)


##### CREATED BY QUEEN SHABAZZ