import os
import sys
from Configuration import Configuration
import smtplib   

class Email:
    #This function sends an e-mail with the given message.  
        
    config = Configuration()
    
    fromaddr = config.fromaddr
    toaddr  = config.toaddr
    subject = 'WARNING: Error Detected!!'
    
    headers = ["From: " + fromaddr,
               "Subject: " + subject,
               "To: " + toaddr,
               "MIME-Version: 1.0",
               "Content-Type: text/html"]
    headers = "\r\n".join(headers)
    
    username = config.username
    password = config.password
        
    server = smtplib.SMTP(config.server)
    server.starttls()
    server.login(username,password)
    server.sendmail(fromaddr,toaddr,headers+"\r\n\r\n")
    server.quit()
