'''
Created on Mar 6, 2013

@author: Sujen
'''
from FileManager import FileManager
from Rule import Rule
from mimify import File
from QueryManager import QueryManager
from Trigger import Trigger
import thread
import operator
import time
import re
import sys
from cgi import logfile
from Configuration import Configuration
from core.Rule import Rule
from robotparser import RuleLine

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
        

    def monitor(self, configuration, rule):
        fm = FileManager()
        queryManager = QueryManager()
        logFile = fm.read(configuration.firewallLog)
        queryManager.mainResult = logFile 
        endPoint = len(logFile)
        
        while (True):
            print "----------------------------------------------------------------------------"
            print rule
            if (endPoint > queryManager.startAt):
                print str(queryManager.startAt)+"BQQQQQQQQQQQQQQQQQQQQQ"
                print "---------------------------------------------------------------------------+"
                if(queryManager.execute(rule)):
                    print "WAZAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
                else:
                    print "No trigger..."
                
                  
            queryManager.startAt = endPoint
            time.sleep(10)
            
            logFile = fm.read(configuration.firewallLog)
            queryManager.mainResult = logFile 
            print str(len(queryManager.mainResult))+"Vince\n"+str(queryManager.startAt)
            endPoint = len(logFile)

    def testMonitoring(self):
        configuration = Configuration()
        ruleManager = Rule()
                
        for rulefile in configuration.ruleFiles:
            useRule = configuration.ruleDir + rulefile
            ruleManager.query = ruleManager.readRules(useRule)
            allRules = ruleManager.ruleList
            
        for i in range(0, len(ruleManager.ruleList)):
            self.monitor(configuration, allRules[i])