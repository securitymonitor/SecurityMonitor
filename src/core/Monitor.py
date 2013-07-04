'''
Created on Mar 6, 2013

@author: Sujen
'''
from FileManager import FileManager
from Rule import Rule
from mimify import File
from QueryManager import QueryManager
from core.Trigger import Trigger
from threading import Thread
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
    Monitor:
        The Monitor class performs the monitoring actions of log files.
    '''
    endPoint = 0
        
    def __init__(self):
        '''
        Constructor
        '''                   

    '''
    This function is a parser for each time a change in the log file occurs.
    '''
    def monitor(self, rule, interval):
        configuration = Configuration()
        fm = FileManager()
        queryManager = QueryManager()
        triggerObj = Trigger()
        logFile = fm.read(configuration.firewallLog)
        queryManager.mainResult = logFile 
        endPoint = len(logFile)
        
        while (True):
            configuration = Configuration()
            print rule
            if (endPoint > queryManager.startAt):
                if(queryManager.execute(rule)):
                    triggerObj.ExecuteTrigger(rule)
                    print "Attack detected!"                  
                else:
                    print "No attack detected..."
                  
            queryManager.startAt = endPoint
            time.sleep(interval)
            
            logFile = fm.read(configuration.firewallLog)
            del queryManager.mainResult[:] 
            
            for i in range(queryManager.startAt, len(logFile)):
                queryManager.mainResult.append(logFile[i])
            
            endPoint = len(logFile)
    
    
    '''
    This function starts the monitoring of the log file.
    '''
    def startMonitoring(self):
        configuration = Configuration()
        ruleManager = Rule()
         
        #Iterates through every rule file in the given directory.      
        for rulefile in configuration.ruleFiles:
            useRule = configuration.ruleDir + rulefile
            ruleManager.query = ruleManager.readRules(useRule)
            allRules = ruleManager.ruleList
        
        #Starts a monitoring thread for each defined rule. The parameters that are used to start a monitor are rule and interval.   
        for i in range(0, len(ruleManager.ruleList)):
            a = Thread(target=self.monitor, args=(allRules[i], ruleManager.interval))
            a.start()
            print str(a)