'''
Created on 4 apr. 2013

@author: Sujen
'''
import os
import sys

os.getcwd()
os.chdir('..')
sys.path.append(os.getcwd())
from core.SMI import SMI


class Email:
    smi = SMI()
    #This function sends an e-mail with the given message.
    import smtplib  
    fromaddr = smi.config.fromaddr 
    toaddr  = smi.config.toaddr  
    subject = 'WARNING: Error Detected!!'
    
    headers = ["From: " + fromaddr,
               "Subject: " + sys.argv[5],
               "To: " + toaddr,
               "MIME-Version: 1.0",
               "Content-Type: text/html"]
    headers = "\r\n".join(headers)
    
    username = smi.config.username
    password = smi.config.password  
    
    server = smtplib.SMTP(smi.config.server)  
    server.starttls() 
    server.login(username,password) 
    server.sendmail(fromaddr,toaddr,headers+"\r\n\r\n"+sys.argv[3])  
    server.quit() 
