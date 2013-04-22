'''
Created on 4 apr. 2013

@author: Sujen
'''
class Email:
    
    #This function sends an e-mail with the given message.
    def SendMail(self,mailBody):
        import smtplib  

        fromaddr = 'hvaminorfis@gmail.com'  
        toaddrs  = 'hvaminorfis@gmail.com'  
        subject = 'WARNING: Error Detected!!'
        
        headers = ["From: " + fromaddr,
                   "Subject: " + subject,
                   "To: " + toaddrs,
                   "MIME-Version: 1.0",
                   "Content-Type: text/html"]
        headers = "\r\n".join(headers)
        
        username = 'hvaminorfis@gmail.com'
        password = 'security1234'  

        server = smtplib.SMTP('smtp.gmail.com:587')  
        server.starttls() 
        server.login(username,password) 
        server.sendmail(fromaddr,toaddrs,headers+"\r\n\r\n"+mailBody)  
        server.quit() 