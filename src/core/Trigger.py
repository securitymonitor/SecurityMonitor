'''
Created on 12 mrt. 2013

@author: Sujen
'''
from core.Configuration import Configuration
from core.Definition import Definitions
import sys
import subprocess

class Trigger:
    action = ""
    data = ""
    description = ""
    mac = ""
    name = ""
    protocol = ""
    sourceip = ""
    sourcept = ""
    targetip = ""
    targetpt = "" 
    
    current = ""
                
    #This executes the appropriate trigger regarding the error.
    def ExecuteTrigger(self, query):     
        config = Configuration()
        definition = Definitions()
        
        while (query != ""):
            
            self.current = query.split("\n")[0]
            #print "current = self.currentrent  
            if self.current.__contains__("ACTION ="):  
                self.action = self.current.split("=")[1].strip().replace("'", "").replace("=", "").strip()
                query = query.replace(self.current, "")
                    
            if self.current.__contains__("DATA ="):  
                self.data = self.current.split("=")[1].strip().replace("'", "").replace("=", "").strip()
                query = query.replace(self.current, "")
                          
            if self.current.__contains__("DESCRIPTION ="):  
                self.description = self.current.split("=")[1].strip().replace("'", "").replace("=", "").strip()
                query = query.replace(self.current, "")
            
            if self.current.__contains__("MAC ="):  
                self.mac = self.current.split("=")[1].strip().replace("'", "").replace("=", "").strip()
                query = query.replace(self.current, "")
                
            if self.current.__contains__("NAME ="):  
                self.name = self.current.split("=")[1].strip().replace("'", "").replace("=", "").strip()
                query = query.replace(self.current, "")
                
            if self.current.__contains__("PROTO ="):  
                self.protocol = self.current.split("=")[1].strip().replace("'", "").replace("=", "").strip()
                query = query.replace(self.current, "")
            
            if self.current.__contains__("SOURCEIP ="):  
                self.sourceip = self.current.split("=")[1].strip().replace("'", "").replace("=", "").strip()
                query = query.replace(self.current, "")
                
            if self.current.__contains__("SOURCEPT ="):  
                self.sourcept = self.current.split("=")[1].strip().replace("'", "").replace("=", "").strip()
                query = query.replace(self.current, "")
                
            if self.current.__contains__("TARGETIP ="):  
                self.targetip = self.current.split("=")[1].strip().replace("'", "").replace("=", "").strip()
                query = query.replace(self.current, "")
                
            if self.current.__contains__("TARGETPT ="):  
                self.targetpt = self.current.split("=")[1].strip().replace("'", "").replace("=", "").strip()
                query = query.replace(self.current, "")

                
            #Remove current from query to continue with next line    
            query = query.replace(self.current, "").replace("\n", "", 1)
        
        print str(len(config.actionFiles)) + "----" + self.action      
        
        for i in range(0,len(config.actionFiles)):
            print str(config.actionFiles[i]) + "----" + self.action  
            if(config.actionFiles[i] == self.action):
                path = config.actionDir + self.action
                print str(path)
                subprocess.call([sys.executable, path, self.action, self.data, self.description, self.mac, self.name, self.protocol, self.sourceip, self.sourcept, self.targetip, self.targetpt])
            else:
                print "nee"
        
        #for i in range(0, len(listModules))
        #    if(listModules[i] == rulemanager.action)
        #        sendmail
            
        #if "Email" == rulemanger.action:
        #    emailObj.SendMail(errorMsg)
        #elif errorType == 5:
        #    pass
        #elif errorType == 10:
        #    pass
        
   