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
    QueryManager:
        This class is used to execute regex search function for each rule.
        Using the keywords defined in definitions, a query filtering will be executed.
        The results of the execution are added to the main result.
        
        countValue                    = Value of count given in the rule.
        countOperator                 = Type operator for the count given in the rule.
        timerValue                    = Value of time given in the rule.
        isLandAttack                  = Defines if the there is a land attack.
        timerOperator                 = Type operator for the time given in the rule.
        startAt                       = Defines the starting line of the changed log file.
        mainResult                    = Filtered data from the query on query search.
        tmpMainResult                 = Temporary list before data is added to main result.
        current                       = This is the rule, with a changing keyword each time it goes through the loop.
        operators                     = This is a list that contains the used operators.
    '''
    
    countValue = 0
    countOperator = ""
    timerValue = 0
    isLandAttack = 0
    timerOperator = ""
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
    
    '''
    This function performs the query on query filtering over the given data.
    '''
    def execute(self, query):
        #Looping until all query lines are executed and removed
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
                if self.current.__contains__("SOURCEIP"):
                    self.isLandAttack = 1
                    print self.isLandAttack
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
            return self.finalize()
        elif(len(self.mainResult) != 0):
            print str(self.mainResult)
            return True
        else:
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
        
        if self.current.__contains__("*") or self.current.__contains__("SOURCEIP"):
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
    
    
    '''
    This function gets the value for the given operator.
    '''
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
    
    '''
    This function executes regex and appends the results to the main result.
    '''    
    def executeRegex(self, regex):
        temp = []  
         
        for i in range(0,len(self.mainResult)):
            if(re.search(regex, str(self.mainResult[i]))):
                if self.isLandAttack:
                    tmpSourceIP = self.mainResult[i].split(Definitions.getValueDefinition("SOURCEIP"))[1].split(" ")[0]
                    tmpTargetIP = self.mainResult[i].split(Definitions.getValueDefinition("TARGETIP"))[1].split(" ")[0]
                    if(tmpSourceIP == tmpTargetIP):
                        temp.append(self.mainResult[i])
                else:
                    temp.append(self.mainResult[i])
                
                    
      
        self.mainResult = None
        self.mainResult = [] 
        for i in range(0,len(temp)):
            self.mainResult.append(temp[i])  
        temp = None
    
    '''
    This function check if there is any input for count and timer.
    '''
    def timeCountIsValid(self):
        return self.countValue != 0 and self.countOperator != "" and self.timerValue != "" and self.timerOperator != ""
    
    '''
    This function is performed if there are any values given for count and timer.
    It checks whether the amount of connections is within a certain timespan.
    '''
    def finalize(self):
        from Monitor import Monitor
        monitor = Monitor()
        
        if(self.operators[self.countOperator](len(self.mainResult), self.countValue)):
            regexDateTime = Definitions.getValueDefinition("DATETIME")
            regexTime = Definitions.getValueDefinition("TIME")
            
            startDateTime = re.findall(regexDateTime, self.mainResult[0])
            endDateTime = re.findall(regexDateTime, self.mainResult[-1])
            
            startTime = re.findall(regexTime, startDateTime[0]) 
            endTime = re.findall(regexTime, endDateTime[0]) 
            
            startTimeSplit = startTime[0].split(":")
            endTimeSplit = endTime[0].split(":")

            hoursToMinutes = 0
            
            if(int(endTimeSplit[0]) > int(startTimeSplit[0])):
                hours = int(endTimeSplit[0]) - int(startTimeSplit[0])
                hoursToMinutes = int(hours)*60
            
            if(int(endTimeSplit[1]) > int(startTimeSplit[1])):
                minutes = int(endTimeSplit[1]) - int(startTimeSplit[1])
                minutes = minutes + hoursToMinutes
                endTimeSplit[2] = int(endTimeSplit[2]) + (60 * minutes)
                
                timeRange = int(endTimeSplit[2]) - int(startTimeSplit[2])  
            else:
                timeRange = int(endTimeSplit[2]) - int(startTimeSplit[2])  
                
            if(self.operators[self.timerOperator](int(timeRange), self.timerValue)):
                return True
            
            else:
                return False  
        else:
            return False
