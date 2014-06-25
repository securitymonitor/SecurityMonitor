import os
import sys

os.getcwd()
os.chdir('../core')

sys.path.append(os.getcwd())

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
    
    if username != "" and password != "":
        pass
        server.starttls()
        server.ehlo() 
        server.login(username,password)     
    else:
        pass

    server.sendmail(fromaddr,toaddr,headers+"\r\n\r\n"+sys.argv[1])
    server.quit()
