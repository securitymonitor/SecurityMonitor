'''
Created on Mar 6, 2013

@author: Sujen
'''
from FileManager import FileManager
from Rule import Rule
from mimify import File
from QueryManager import QueryManager
from Trigger import Trigger
import operator
import time
import re
import sys
from cgi import logfile
from Configuration import Configuration

class Monitor:
    '''
    classdocs
    '''
    endPoint = 0
    def __init__(self):
        #fileManager.read()
        '''
        Constructor
        '''            
    #Recursive function in order to keep the process going infinitely.    
    def keepMonitoring(self,oldMaxLines,dirConfig,dirLog):
        import time
        fileManager = FileManager()
        monitorObj = Monitor()
        logLines = fileManager.read(dirLog)
        
        if(oldMaxLines == len(logLines)):
            print "The log file still hasn't changed."
            time.sleep(10)
            monitorObj.keepMonitoring(oldMaxLines,dirConfig,dirLog)
        else:
            print "The log file still has changed."
            startAt = oldMaxLines
            monitorObj.testMonitoring(dirConfig, dirLog, startAt)
        
    def stopMonitoring(self):        
        print "Monitoring Ended!"
        time.sleep(10)
        sys.exit(0)
        
    def testMonitoring(self):
        import threading
        configuration = Configuration()
        ruleManager = Rule()
        queryManager = QueryManager()
        fm = FileManager()
        logFile = fm.read(configuration.firewallLog)  
        queryManager.mainResult = logFile 
    
        #ruleManager.readRules(configuration.ruleFile)
        self.endPoint = len(logFile)

        while(True):
            if(self.endPoint > queryManager.startAt):
                print "logfile has changed"
                
                for ruleFile in range(len(configuration.ruleFiles)): 
                    configuration.ruleFiles[ruleFile].strip("'")
                    useRule = configuration.ruleDir + configuration.ruleFiles[ruleFile]
                    ruleManager.readRules(useRule)
                    print useRule
                    print "Monitoring using the rule " + ruleManager.name + "...\n"
                    print ruleManager.query
                    
                    if(queryManager.execute(ruleManager.query)):
                        print "WAZAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
                    
                queryManager.startAt = self.endPoint
                #trigger(rulemanager.action, )
            else:
                print "logfile has not changed"
                
            time.sleep(10)
            logFile = fm.read(configuration.firewallLog)
            queryManager.mainResult = logFile
            print str(len(logFile))
            print str(len(queryManager.mainResult))
            self.endPoint = len(logFile)
