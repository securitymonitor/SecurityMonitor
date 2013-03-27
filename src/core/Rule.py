'''
Created on Mar 6, 2013

@author: Sujen
'''
from core.FileManager import FileManager

class Rule:

    fileManager = FileManager()
    regex = fileManager.read("Rules.txt")
    
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
                
    regexFile = open("Rules.txt")
    var1 = checkEntry('',regexFile)
