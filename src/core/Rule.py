'''
Created on Mar 6, 2013

@author: vinesh
'''
from core.FileManager import FileManager

class Rule:

    fileManager = FileManager()
    regex = fileManager.read("Rules.txt")
    
    def __init__(self):
        '''
        Constructor
        '''
        
    def delete(self,dirConfig,ruleId):
        fileManager = FileManager()
        regexList = fileManager.read(dirConfig)
        file = open(dirConfig,"r+")
        
        del regexList[ruleId]
        
        #regexList = [word.strip() for word in regexList]
        
        file.truncate()
        for i in range(0,len(regexList)):
            file.write(regexList[i])
            
        print regexList
            
        
    def test(self):
        print "Rule created."
        