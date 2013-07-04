'''
Created on Mar 6, 2013

@author: Sujen
'''
from core.FileManager import FileManager
from core.Definition import Definitions
from robotparser import RuleLine
from core.Configuration import Configuration

class Rule:
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
    def addRule(self,dirConfig,newRule):
        fileManager = FileManager()
        regexList = fileManager.read(dirConfig)
        file = open(dirConfig,"r+")
        regexList.append(newRule+"\n")
        fileManager.overwrite(regexList, file)

    def editRule(self,dirConfig,ruleId,newRule):
        fileManager = FileManager()
        regexList = fileManager.read(dirConfig)
        file = open(dirConfig,"r+")
        ruleId = ruleId - 1
        regexList[ruleId] = newRule+"\n"  
        fileManager.overwrite(regexList, file)
    
    def deleteRule(self,dirConfig,ruleId):
        fileManager = FileManager()
        regexList = fileManager.read(dirConfig)
        file = open(dirConfig,"r+")
        ruleId = ruleId - 1
        del regexList[ruleId]
        fileManager.overwrite(regexList, file)   
    
    def test(self):
        print "Rule created."
        
    def checkEntry(self, regexFile):
        print "##Method checkEntry##"
        import re
        from Action import Action

        actionObj = Action()

        for entry in regexFile.readlines():
            print "##entryLine: ", entry
            lnsplit = entry.split(" ")
            
            if entry.__contains__('-t') == 1:
                print '##Condition = True (-t)##' 
            if entry.__contains__('-c') == 1:
                print '##Condition = True (-c)##'
                connection = lnsplit[0]
                print "##Method call Action.checkEntryFrequency()##"
                actionObj.checkEntryFrequency(connection)
    
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