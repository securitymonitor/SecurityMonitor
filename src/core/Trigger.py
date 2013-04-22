'''
Created on 12 mrt. 2013

@author: Sujen
'''
class Trigger:
                
    #This executes the appropriate trigger regarding the error.
    def ExecuteTrigger(self,errorType,errorMsg):     
        from Email import Email
             
        triggerObj = Trigger()
        emailObj = Email()
        
        if errorType == 1:
            emailObj.SendMail(errorMsg)
        elif errorType == 5:
            pass
        elif errorType == 10:
            pass