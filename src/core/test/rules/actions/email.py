import os
import sys


#This function sends an e-mail with the given message.
import smtplib

fromaddr = 'spamchristiaan@gmail.com'
toaddr  = 'spamchristiaan@gmail.com'
subject = 'WARNING: Error Detected!!'

headers = ["From: " + fromaddr,
           "Subject: " + 'test',
           "To: " + toaddr,
           "MIME-Version: 1.0",
           "Content-Type: text/html"]
headers = "\r\n".join(headers)

username = 'spamchristiaan@gmail.com'
password = 

server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr,toaddr,headers+"\r\n\r\n")
server.quit()
