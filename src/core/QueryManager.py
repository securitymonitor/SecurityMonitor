'''
Created on May 28, 2013

@author: vinesh
'''
import re
import operator
from core.Definition import Definitions
from core.Trigger import Trigger
from core.FileManager import FileManager

class QueryManager:
    '''
    The Security Monitoring Query Manager
    '''
    countValue = 0
    countOperator = ""
    timerValue = 0
    timerOperator = ""
    timerQuery = ""
    result = []
    
    def execute(self, query, startAt):

        #Looping until all query lines are executed and removed
        while (query != ""):
            current = query.split("\n")[0]
            #print "current = " + current
            
            if current.__contains__("COUNT"):   
                self.getCount(current, self.result, startAt)
                #print str(len(result))
                query = query.replace(current, "")
            
            if current.__contains__("MAC ="):  
                result = self.getMAC(current, self.result, startAt)
                #print str(len(result))
                query = query.replace(current, "")
            
            if current.__contains__("SOURCEIP ="):  
                result = self.getSourceIP(current, self.result, startAt)
                #print str(len(result))
                query = query.replace(current, "")
                
            if current.__contains__("SOURCEPT ="):  
                result = self.getSourcePT(current, self.result, startAt)
                #print str(len(result))
                query = query.replace(current, "")
                
            if current.__contains__("TARGETIP ="):  
                result = self.getTargetIP(current, self.result, startAt)
                #print str(len(result))
                query = query.replace(current, "")
                
            if current.__contains__("TARGETPT ="):  
                result = self.getTargetPT(current, self.result, startAt)
                #print str(len(result))
                query = query.replace(current, "")
                
            if current.__contains__("TIMER"):  
                result = self.getTimer(current, self.result, startAt)
                #print str(len(result))
                query = query.replace(current, "")
                
            #Remove current from query to continue with next line    
            query = query.replace(current, "").replace("\n", "", 1)
        return self.result
    
    
    def getMAC(self, query, mainResult, startAt):
        regex = Definitions.getValueDefinition("MAC")
        
        if query.__contains__("*"):
            regex = regex + "([a-fA-F0-9]{2}[:|\-]?){6}" #Alle MAC's
        else:
            regex = regex + query.split("=")[1].strip() #gedefineerde MAC's
            
        return self.executeRegex(regex, mainResult, startAt)
    
        
    def getSourceIP(self, query, mainResult, startAt):
        regex = Definitions.getValueDefinition("SOURCEIP")
        
        if query.__contains__("*"):
            regex = regex + "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}" #Alle IP's
        else:
            regex = regex + query.split("=")[1].strip() #gedefineerde IP's
            
        return self.executeRegex(regex, mainResult, startAt)
    
    
    def getTargetIP(self, query, mainResult, startAt):
        regex = Definitions.getValueDefinition("TARGETIP")
        
        if query.__contains__("*"):
            regex = regex + "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}" #Alle IP's
        else:
            regex = regex + query.split("=")[1].strip() #gedefineerde IP's
            
        return self.executeRegex(regex, mainResult, startAt)
    
    
    def getSourcePT(self, query, mainResult, startAt):
        regex = Definitions.getValueDefinition("SOURCEPT")
        
        if query.__contains__("*"):
            regex = regex + "\d" #Alle poorten
        else:
            regex = regex + query.split("=")[1].strip() #gedefineerde poort
            
        return self.executeRegex(regex, mainResult, startAt)
    
    
    def getTargetPT(self, query, mainResult, startAt):
        regex = Definitions.getValueDefinition("TARGETPT")
        
        if query.__contains__("*"):
            regex = regex + "\d" #Alle poorten
        else:
            regex = regex + query.split("=")[1].strip() #gedefineerde poort
            
        return self.executeRegex(regex, mainResult, startAt)
    
        
    def getCount(self, query, mainResult, startAt):
        print query + "\n" + str(mainResult)
        countValue, countOperator = self.getValueByOperator(query)
        #timeOperator = self.getValueByOperator(query)
        self.countValue = int(countValue)
        self.countOperator = countOperator
        self.executeRegex(Definitions.getValueDefinition("COUNT"), mainResult, startAt)
        
        
    def getTimer(self, query, mainResult, startAt):
        timerValue, timerOperator = self.getValueByOperator(query)
        #timeOperator = self.getValueByOperator(query)
        self.timerValue = int(timerValue)
        self.timerOperator = timerOperator
        self.executeRegex(Definitions.getValueDefinition("TIMER"), mainResult, startAt)

    def getValueByOperator(self, query):
            value = 0
            operator = 0
            
            if query.__contains__(">"):
                value = query.split(">")[1].strip()
                operator = ">"
            if query.__contains__("="):
                value = query.split("=")[1].strip()
                operator = "=="
            if query.__contains__("<"):    
                value = query.split("<")[1].strip()
                operator = "<"
            return value, operator

    def executeRegex(self, regex, mainResult, startAt):
        if (len(mainResult) == 0):
            fm = FileManager()
            from Configuration import Configuration
            
            config = Configuration()
            allLines = fm.read(config.FirewallLog)
        else:
            allLines = mainResult
        
        print str(self.countValue) + "\n" + str(self.countOperator) + "\n" + str(self.timerValue) + "\n" + str(self.timerOperator)
        if((self.countValue != 0) and (self.countOperator != "") and (self.timerValue != "") and (self.timerOperator != "")):
            print "-1"
            triggerObj = Trigger()
            
            operators = {
            "==": operator.eq,
            "!=": operator.ne,
            "<>": operator.ne,
            "<": operator.lt,
            "<=": operator.le,
            ">": operator.gt,
            ">": operator.ge
            }
            
            print "0"
            if operators[self.countOperator](len(mainResult), self.countValue):
                print "1"
                regexTime = "\d+:\d+:\d+"
    
                startTime = re.findall(regexTime, mainResult[0]) 
                endTime = re.findall(regexTime, mainResult[-1]) 
                
                startTimeSplit = startTime[0].split(":")
                endTimeSplit = endTime[0].split(":")
                
                if(int(endTimeSplit[1]) > int(startTimeSplit[1])):
                    print "2"
                    minutes = int(endTimeSplit[1]) - int(startTimeSplit[1])
                    endTimeSplit[2] = str(int(endTimeSplit[2]) + (60 * minutes))
                    
                timeRange = int(endTimeSplit[2]) - int(startTimeSplit[2])  
    
                if operators[self.timerOperator](int(timeRange), self.timerValue):
                    print "3"
                    errorType = 1
                    errorMsg = 'Hello Admin,<br /><br />We have detected a possible threat.<br />The file concerning the error is: .<br /><br /><i>This mail has been automatically generated by the</i><b> Security Monitor</b>'
                    triggerObj.ExecuteTrigger(errorType,errorMsg)   
                    print "mail is triggered"
                    return ""  
            
        else:    
            result = []
            
            for i in range(startAt,len(allLines)):
                if(re.search(regex, str(allLines[i]))):
                    result.append(allLines[i])
            return result        