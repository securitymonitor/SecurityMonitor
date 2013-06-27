'''
Created on May 28, 2013

@author: vinesh
'''
import re
import operator
from core.Definition import Definitions
from core.Trigger import Trigger
from core.FileManager import FileManager
from core.Configuration import Configuration


class QueryManager:
    '''
    The Security Monitoring Query Manager
    '''
    countValue = 0
    countOperator = ""
    timerValue = 0
    timerOperator = ""
    timerQuery = ""
    startAt = 0
    mainResult = []
    tmpMainResult = []
    current = ""
    operators = {
        "==": operator.eq,
        "!=": operator.ne,
        "<>": operator.ne,
        "<": operator.lt,
        "<=": operator.le,
        ">": operator.gt,
        ">=": operator.ge
    }
    
    def execute(self, query):
        #Looping until all query lines are executed and removed
        print str(len(self.mainResult)) + "jasper exception"
        print query
        while (query != ""):
            
            self.current = query.split("\n")[0]
            #print "current = self.currentrent
            
            if self.current.__contains__("COUNT"):   
                self.getCount()
                query = query.replace(self.current, "")
                
            if self.current.__contains__("DATA ="):  
                self.getData()
                query = query.replace(self.current, "")
            
            if self.current.__contains__("MAC ="):  
                self.getMAC()
                query = query.replace(self.current, "")
            
            if self.current.__contains__("PROTO ="):  
                self.getProto()
                query = query.replace(self.current, "")
            
            if self.current.__contains__("SOURCEIP ="):  
                self.getSourceIP()
                query = query.replace(self.current, "")
                
            if self.current.__contains__("SOURCEPT ="):  
                self.getSourcePT()
                query = query.replace(self.current, "")
                
            if self.current.__contains__("TARGETIP ="):  
                self.getTargetIP()
                query = query.replace(self.current, "")
                
            if self.current.__contains__("TARGETPT ="):  
                self.getTargetPT()
                query = query.replace(self.current, "")
                
            if self.current.__contains__("TIMER"):  
                self.getTimer()
                query = query.replace(self.current, "")
                
            #Remove current from query to continue with next line    
            query = query.replace(self.current, "").replace("\n", "", 1)
        
        if(self.timeCountIsValid()):
            print "1"
            return self.finalize()
        elif(len(self.mainResult) != 0):
            print "55555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555"
            print "5"
            print str(self.mainResult)
            return True
        else:
            print "66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666"
            return False
    
    
    def getMAC(self):
        regex = Definitions.getValueDefinition("MAC")
        
        if self.current.__contains__("*"):
            regex = regex + "([a-fA-F0-9]{2}[:|\-]?){6}" #Alle MAC's
        else:
            regex = regex + self.current.split("=")[1].strip() #gedefineerde MAC's
            
        return self.executeRegex(regex)
    
    
    def getData(self):
        regex = Definitions.getValueDefinition("DATA")
        
        if self.current.__contains__("*"):
            regex = regex + "" #Alle TCP flag(s)
        else:
            regex = regex + self.current.split("=")[1].strip() #gedefineerde TCP flag(s)
            
        return self.executeRegex(regex)
        
        
    def getProto(self):
        regex = Definitions.getValueDefinition("PROTO")
        
        if self.current.__contains__("*"):
            regex = regex + "" #Alle Protocollen
        else:
            regex = regex + self.current.split("=")[1].strip() #gedefineerde Protocol
                        
        return self.executeRegex(regex)
    
    
    def getSourceIP(self):
        regex = Definitions.getValueDefinition("SOURCEIP")
        
        if self.current.__contains__("*"):
            regex = regex + "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}" #Alle IP's
        else:
            regex = regex + self.current.split("=")[1].strip() #gedefineerde IP's
            
        return self.executeRegex(regex)
    
    
    def getTargetIP(self):
        regex = Definitions.getValueDefinition("TARGETIP")
        
        if self.current.__contains__("*"):
            regex = regex + "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}" #Alle IP's
        else:
            regex = regex + self.current.split("=")[1].strip() #gedefineerde IP's
            
        return self.executeRegex(regex)
    
    
    def getSourcePT(self):
        regex = Definitions.getValueDefinition("SOURCEPT")
        
        if self.current.__contains__("*"):
            regex = regex + "\d" #Alle poorten
        else:
            regex = regex + self.current.split("=")[1].strip() #gedefineerde poort
            
        return self.executeRegex(regex)
    
    
    def getTargetPT(self):
        regex = Definitions.getValueDefinition("TARGETPT")
        
        if self.current.__contains__("*"):
            regex = regex + "\d" #Alle poorten
        else:
            regex = regex + self.current.split("=")[1].strip() #gedefineerde poort
            
        return self.executeRegex(regex)
    
        
    def getCount(self):
        countValue, countOperator = self.getValueByOperator()
        self.countValue = int(countValue)
        self.countOperator = countOperator
        
        
    def getTimer(self):
        timerValue, timerOperator = self.getValueByOperator()
        self.timerValue = int(timerValue)
        self.timerOperator = timerOperator

    def getValueByOperator(self):
            value = 0
            operator = 0
            
            if self.current.__contains__(">"):
                value = self.current.split(">")[1].strip()
                operator = ">"
            if self.current.__contains__("="):
                value = self.current.split("=")[1].strip()
                operator = "=="
            if self.current.__contains__("<"):    
                value = self.current.split("<")[1].strip()
                operator = "<"
            if self.current.__contains__("<="):    
                value = self.current.split("<=")[1].strip()
                operator = "<="
            if self.current.__contains__(">="):    
                value = self.current.split(">=")[1].strip()
                operator = ">="
            return value, operator
        
    def executeRegex(self, regex):
        print regex + "rex"
        temp = []
        
        for i in range(self.startAt,len(self.mainResult)):
            if(re.search(regex, str(self.mainResult[i]))):
                temp.append(self.mainResult[i])
                
        del self.mainResult[:]
        self.mainResult = []
        
        for i in range(0,len(temp)):
            self.mainResult.append(temp[i])
        
        print "na del mainres is " + str(len(self.mainResult))

    def timeCountIsValid(self):
        return self.countValue != 0 and self.countOperator != "" and self.timerValue != "" and self.timerOperator != ""

    def finalize(self):
        from Monitor import Monitor
        monitor = Monitor()
        print "-------- "+str(self.countOperator)+" -------- "+str(len(self.mainResult))+" --------------- "+str(self.countValue)
        
        if(self.operators[self.countOperator](len(self.mainResult), self.countValue)):
            print "2"
            print "-------------"+str(self.countOperator)+"-------------"+str(self.countValue)+"-------------"+str(len(self.mainResult))
            regexDateTime = Definitions.getValueDefinition("DATETIME")
            regexTime = Definitions.getValueDefinition("TIME")
            
            startDateTime = re.findall(regexDateTime, self.mainResult[0])
            endDateTime = re.findall(regexDateTime, self.mainResult[-1])
            
            startTime = re.findall(regexTime, startDateTime[0]) 
            endTime = re.findall(regexTime, endDateTime[0]) 
            
            startTimeSplit = startTime[0].split(":")
            endTimeSplit = endTime[0].split(":")
            
            print str(startTime)
            print str(endTime)
            
            if(int(endTimeSplit[1]) > int(startTimeSplit[1])):
                print "3"
                minutes = int(endTimeSplit[1]) - int(startTimeSplit[1])
                endTimeSplit[2] = int(endTimeSplit[2]) + (60 * minutes)
                
                timeRange = int(endTimeSplit[2]) - int(startTimeSplit[2])  
            else:
                timeRange = int(endTimeSplit[2]) - int(startTimeSplit[2])  
                
            if(self.operators[self.timerOperator](int(timeRange), self.timerValue)):
                print "True!!!!!!!!!!!!! 01"
                print "-------------"+str(self.timerValue)+"-------------"+str(self.timerOperator)+"-------------"
                return True
            
            else:
                return False  
        else:
            return False
