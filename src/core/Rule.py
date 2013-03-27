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
        