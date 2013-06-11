'''
Created on 12 mrt. 2013

@author: Sujen
'''
class Trigger:
                
    #This executes the appropriate trigger regarding the error.
    def ExecuteTrigger(self,errorType,errorMsg):     
        from custom.actions.Email import Email
             
        triggerObj = Trigger()
        emailObj = Email()
        
        listModules = fm.Read(Config.txt)
        
        for i in range(0, len(listModules))
            if(listModules[i] == rulemanager.action)
                sendmail
            
        if "Email" == rulemanger.action:
            emailObj.SendMail(errorMsg)
        elif errorType == 5:
            pass
        elif errorType == 10:
            pass