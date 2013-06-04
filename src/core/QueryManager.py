'''
Created on May 28, 2013

@author: vinesh
'''
import re
from core.Definition import Definitions
from core.FileManager import FileManager

class QueryManager:
    '''
    The Security Monitoring Query Manager
    '''
    
    
    def execute(self, query, startAt):
        result = []
        
        #Looping until all query lines are executed and removed
        while (query != ""):
            current = query.split("\n")[0]
            print "current = " + current
            
            if current.__contains__("COUNT"):   
                self.getCount(current, result, startAt)
                print str(len(result))
                query = ""
            
            if current.__contains__("MAC ="):  
                result = self.getMAC(current, result, startAt)
                print str(len(result))
                query = query.replace(current, "")
            
            if current.__contains__("SOURCEIP ="):  
                result = self.getSourceIP(current, result, startAt)
                print str(len(result))
                query = query.replace(current, "")
                
            if current.__contains__("SOURCEPT ="):  
                result = self.getSourcePT(current, result, startAt)
                print str(len(result))
                query = query.replace(current, "")
                
            if current.__contains__("TARGETIP ="):  
                result = self.getTargetIP(current, result, startAt)
                print str(len(result))
                query = query.replace(current, "")
                
            if current.__contains__("TARGETPT ="):  
                result = self.getTargetPT(current, result, startAt)
                print str(len(result))
                query = query.replace(current, "")
               
            if current.__contains__("TIME"):  
                result = self.getTime(current, result, startAt)
                print str(len(result))
                query = query.replace(current, "")
                
            #Remove current from query to continue with next line    
            query = query.replace(current, "").replace("\n", "", 1)
        return result
    
    
    def getMAC(self, query, mainResult, startAt):
        regex = Definitions.getValueDefinition("MAC")
        
        if query.__contains__("*"):
            regex = regex + "([a-fA-F0-9]{2}[:|\-]?){6}" #Alle MAC's
        else:
            regex = regex + query.split("=")[1].strip() #gedefineerde MAC's
            
        return self.executeRegex(regex, mainResult, 0, startAt)
    
        
    def getSourceIP(self, query, mainResult, startAt):
        regex = Definitions.getValueDefinition("SOURCEIP")
        
        if query.__contains__("*"):
            regex = regex + "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}" #Alle IP's
        else:
            regex = regex + query.split("=")[1].strip() #gedefineerde IP's
            
        return self.executeRegex(regex, mainResult, 0, startAt)
    
    
    def getTargetIP(self, query, mainResult, startAt):
        regex = Definitions.getValueDefinition("TARGETIP")
        
        if query.__contains__("*"):
            regex = regex + "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}" #Alle IP's
        else:
            regex = regex + query.split("=")[1].strip() #gedefineerde IP's
            
        return self.executeRegex(regex, mainResult, 0, startAt)
    
    
    def getSourcePT(self, query, mainResult, startAt):
        regex = Definitions.getValueDefinition("SOURCEPT")
        
        if query.__contains__("*"):
            regex = regex + "\d" #Alle poorten
        else:
            regex = regex + query.split("=")[1].strip() #gedefineerde poort
            
        return self.executeRegex(regex, mainResult, 0, startAt)
    
    
    def getTargetPT(self, query, mainResult, startAt):
        regex = Definitions.getValueDefinition("TARGETPT")
        
        if query.__contains__("*"):
            regex = regex + "\d" #Alle poorten
        else:
            regex = regex + query.split("=")[1].strip() #gedefineerde poort
            
        return self.executeRegex(regex, mainResult, 0, startAt)
    
        
    def getCount(self, query, mainResult, startAt):
        if query.__contains__("SOURCEIP"):
                        
            if query.__contains__(">"):
                count = query.split(">")[1].strip()
            if query.__contains__("="):
                count = query.split("=")[1].strip()
            if query.__contains__("<"):    
                count = query.split("<")[1].strip()
                
                self.executeRegex(Definitions.getValueDefinition("SOURCEIP"), mainResult, count, startAt)
                
        print "result = " + str(count)
        
        
    def getTime(self, query, mainResult, startAt):
        if query.__contains__("TIME"):
                        
            if query.__contains__(">"):
                count = query.split(">")[1].strip()
            if query.__contains__("="):
                count = query.split("=")[1].strip()
            if query.__contains__("<"):    
                count = query.split("<")[1].strip()
                
                self.executeRegex(Definitions.getValueDefinition("TIME"), mainResult, count, startAt)
                
        print "result = " + str(count)

            
    def executeRegex(self, regex, mainResult, count, startAt):
        if (len(mainResult) == 0):
            fm = FileManager()
            from Configuration import Configuration
            
            config = Configuration()
            allLines = fm.read(config.FirewallLog)
        else:
            allLines = mainResult
        
        result = []
        
        for i in range(startAt,len(allLines)):
            if(re.search(regex, str(allLines[i]))):
                result.append(allLines[i])
            
        return result        