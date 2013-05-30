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
    
    
    def execute(self, query):
        result = []
        
        #Looping until all query lines are executed and removed
        while (query != ""):
            current = query.split("\n")[0]
            print "current = " + current
            
            if current.__contains__("COUNT"):   
                self.getCount(current, result)
                print str(len(result))
                query = ""
            
            if current.__contains__("MAC ="):  
                result = self.getSourceIP(current, result)
                print str(len(result))
                query = query.replace(current, "")
            
            if current.__contains__("SOURCEIP ="):  
                result = self.getSourceIP(current, result)
                print str(len(result))
                query = query.replace(current, "")
                
            if current.__contains__("SOURCEPT ="):  
                result = self.getSourcePT(current, result)
                print str(len(result))
                query = query.replace(current, "")
                
            if current.__contains__("TARGETIP ="):  
                result = self.getTargetIP(current, result)
                print str(len(result))
                query = query.replace(current, "")
                
            if current.__contains__("TARGETPT ="):  
                result = self.getTargetPT(current, result)
                print str(len(result))
                query = query.replace(current, "")
                
            if current.__contains__("TIME"):   
                result = self.getTime(current, result)
                print str(len(result))
                query = query.replace(current, "")
                
            #Remove current from query to continue with next line    
            query = query.replace(current, "").replace("\n", "", 1)
        return result
    
    
    def getMAC(self, query, mainResult):
        regex = Definitions.getValueDefinition("MAC")
        
        if query.__contains__("*"):
            regex = regex + "([a-fA-F0-9]{2}[:|\-]?){6}" #Alle MAC's
        else:
            regex = regex + query.split("=")[1].strip() #gedefineerde MAC's
            
        return self.executeRegex(regex, mainResult)
    
        
    def getSourceIP(self, query, mainResult):
        regex = Definitions.getValueDefinition("SOURCEIP")
        
        if query.__contains__("*"):
            regex = regex + "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}" #Alle IP's
        else:
            regex = regex + query.split("=")[1].strip() #gedefineerde IP's
            
        return self.executeRegex(regex, mainResult, 0)
    
    
    def getTargetIP(self, query, mainResult):
        regex = Definitions.getValueDefinition("TARGETIP")
        
        if query.__contains__("*"):
            regex = regex + "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}" #Alle IP's
        else:
            regex = regex + query.split("=")[1].strip() #gedefineerde IP's
            
        return self.executeRegex(regex, mainResult)
    
    
    def getSourcePT(self, query, mainResult):
        regex = Definitions.getValueDefinition("SOURCEPT")
        
        if query.__contains__("*"):
            regex = regex + "\d" #Alle poorten
        else:
            regex = regex + query.split("=")[1].strip() #gedefineerde poort
            
        return self.executeRegex(regex, mainResult)
    
    
    def getTargetPT(self, query, mainResult):
        regex = Definitions.getValueDefinition("TARGETPT")
        
        if query.__contains__("*"):
            regex = regex + "\d" #Alle poorten
        else:
            regex = regex + query.split("=")[1].strip() #gedefineerde poort
            
        return self.executeRegex(regex, mainResult)
    
        
    def getCount(self, query, mainResult):
        if query.__contains__("SOURCEIP"):
                        
            if query.__contains__(">"):
                count = query.split(">")[1].strip()
            if query.__contains__("="):
                count = query.split("=")[1].strip()
            if query.__contains__("<"):    
                count = query.split("<")[1].strip()
                
                self.executeRegex(Definitions.getValueDefinition("SOURCEIP"), mainResult, count)
                
        print "result = " + str(count)
        
        
    def getTime(self, query, mainResult):
        if query.__contains__("TIME"):
                        
            if query.__contains__(">"):
                count = query.split(">")[1].strip()
            if query.__contains__("="):
                count = query.split("=")[1].strip()
            if query.__contains__("<"):    
                count = query.split("<")[1].strip()
                
                self.executeRegex(Definitions.getValueDefinition("TIME"), mainResult, count)
                
        print "result = " + str(count)
                
            
            
    def executeRegex(self, regex, mainResult, count):
        if (len(mainResult) == 0):
            fm = FileManager()
            allLines = fm.read("TestFirewall.log")
        else:
            allLines = mainResult
        
        result = []
        
        for i in range(0,len(allLines)):
            if(re.search(regex, str(allLines[i]))):
                result.append(allLines[i])
            
        return result        