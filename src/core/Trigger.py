'''
Created on 12 mrt. 2013

@author: Sujen
'''
class Trigger:
        
    #This function sends an e-mail with the given message.
    def Notify(self,mailBody):
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
                
    #This executes the appropriate trigger regarding the error.
    def executeTrigger(self,errorType,errorMsg):     
        triggerObj = Trigger()
        if errorType == 1:
            triggerObj.Notify(errorMsg)
        elif errorType == 5:
            pass
        elif errorType == 10:
            pass