'''
Created on Mar 6, 2013

@author: Sujen
'''
from core.FileManager import FileManager
from core.Rule import Rule
from mimify import File
from core.QueryManager import QueryManager
from core.Trigger import Trigger
import operator
import time
import re
import sys
from cgi import logfile
from core.Configuration import Configuration

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
        configuration = Configuration()
        ruleManager = Rule()
        queryManager = QueryManager()
        fm = FileManager()
        logFile = fm.read(configuration.firewallLog)  
        queryManager.mainResult = logFile 
    
        ruleManager.readRules(configuration.ruleFile)
        self.endPoint = len(logFile)
        
        print "Monitoring using the rule " + ruleManager.name + "...\n"
        print ruleManager.query
        
        #queryManager.execute(ruleManager.query)

        while(True):
            if(self.endPoint > queryManager.startAt):
                print "logfile has changed"
                if(queryManager.execute(ruleManager.query)):
                    print "WAZAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
                    
                queryManager.startAt = self.endPoint
                #trigger(rulemanager.action, )
            else:
                print "logfile has not changed"
                
            time.sleep(10)
            logFile = fm.read(configuration.firewallLog)
            queryManager.mainResult = logFile
            self.endPoint = len(logFile)
