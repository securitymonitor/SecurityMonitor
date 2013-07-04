'''
Created on Mar 6, 2013

@author: Sujen
'''
from core.FileManager import FileManager
from core.Definition import Definitions
from robotparser import RuleLine
from core.Configuration import Configuration

class Rule:
    '''
    Rule:
        This class defines a rule by reading the data within the curly brackets.
        
        config                = Instance of the Configuration class.
        interval              = Defines the interval per rule. If it isn't defined it will get a default value from the config.
        query                 = The query contains keywords with a corresponding value.
        startAt               = Defines the starting line of the changed log file.
        ruleList              = List for all files in the rule directory.
        fileManager           = Instance of the FileManager class.
    '''
    
    config = Configuration()
    interval = config.interval
    query = ""
    startAt = 0
    ruleList = []
    
    fileManager = FileManager()
    #regex = fileManager.read("Rules.txt")
    
    def __init__(self):
        '''
        Constructor
        '''
    
    #Gets the definition value
    def getValue(self, entry, definition):
        split = entry.split(definition)
        value = split[1].replace("'", "").replace("=", "").strip()
        return value
                
    def readRules(self, rules):
        fileManager = FileManager()
        rulesList = fileManager.read(rules)
        query = ""
        inRule = 0
               
        if(len(rulesList) > self.startAt): 
            for entry in range(self.startAt, len(rulesList)):
                if inRule == 0:
                    if rulesList[entry].__contains__('{') == 1: #Start of a rule.
                        inRule = 1
                else:
                    if rulesList[entry].__contains__('}') == 1: #End of a rule.
                        inRule = 0
                        self.ruleList.append(query)
                        query = ""

                #Get the name, description and action from the rule, build query
                if (inRule):
                    if rulesList[entry].__contains__('{') == 0:
                        query = query + rulesList[entry]

                        if rulesList[entry].__contains__('INTERVAL'):
                            strInterval = rulesList[entry].split("=")[1]
                            
                            if(strInterval.__contains__(":")):
                                timeInterval = strInterval.split(":")
                                hoursExist = True
                                minutesExist = True
                                
                                if(len(timeInterval) == 3): 
                                    hoursExist = True
                                elif(len(timeInterval) == 2):
                                    hoursExist = False
                                    minutesExist = True
                                else:
                                    hoursExist = False
                                    minutesExist = False
                                    
                                if(hoursExist):
                                    hour = int(timeInterval[0])
                                    min = int(timeInterval[1])                       
                                    sec = int(timeInterval[2])
                                    self.interval = (int(hour)*60*60)+(int(min)*60)+int(sec)
                                elif(minutesExist):
                                    min = int(timeInterval[0])
                                    sec = int(timeInterval[1])
                                    self.interval = (int(min)*60)+(int(sec))
                                                                                                                  
                            else:
                                self.interval = int(strInterval)
                             

                self.query = query