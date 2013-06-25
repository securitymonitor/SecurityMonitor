'''
Created on Mar 6, 2013

@author: Sujen
'''
from core.FileManager import FileManager
from core.Definition import Definitions

class Rule:
    name = ""
    description = ""
    action = ""
    query = ""
    
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
                
    #regexFile = open("Rules.txt")
    #var1 = checkEntry('',regexFile)
    
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
        
        for entry in rulesList:
            if inRule == 0:
                if entry.__contains__('{') == 1: #Start of a rule.
                    inRule = 1

            else:
                if entry.__contains__('}') == 1: #End of a rule.
                    inRule = 0
                    break
                
                #Get the name, description and action from the rule, build query
                if entry.__contains__('NAME') == 1:
                    value = self.getValue(entry, 'NAME')
                    self.name = value
                elif entry.__contains__('DESCRIPTION') == 1:
                    value = self.getValue(entry, 'DESCRIPTION')
                    self.description = value
                elif entry.__contains__('ACTION') == 1:
                    value = self.getValue(entry, 'ACTION')
                    self.action = value
                else:
                    query = query + entry
                    
        self.query = query