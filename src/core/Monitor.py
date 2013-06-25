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
import Queue
from cgi import logfile
from Configuration import Configuration

class Monitor:
    '''
    classdocs
    '''
    endPoint = 0
    threadQueue = Queue.Queue()
        
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
        queryManager.tmpMainResult = list(queryManager.mainResult)
        #ruleManager.readRules(configuration.ruleFile)
        self.endPoint = len(logFile)
        
        print "-----> 01 " + str(len(queryManager.mainResult))
        print "-----> 01 " + str(len(queryManager.tmpMainResult))
        
        while(True):
            if(self.endPoint > queryManager.startAt):
                print "startat 1 " + str(queryManager.startAt)
                print "logfile has changed"
                
                for rulefile in configuration.ruleFiles:
                        splitrule = rulefile.strip("'")
                        useRule = configuration.ruleDir + splitrule
                        ruleManager.readRules(useRule)
                         
                        #print "startat 2 " + str(queryManager.startAt)
                        print "-----> 02 " + str(len(queryManager.mainResult))
                        print "-----> 02 " + str(len(queryManager.tmpMainResult))
                        print "Monitoring using the rule " + ruleManager.name + "...\n"
                        print ruleManager.query
                        
                        queryManager.execute(ruleManager.query)
                        #thread.start_new(queryManager.execute, (ruleManager.query,))
                        #print str(queryManager.mainResult)
                        trueFalse = self.threadQueue.get()
                        print "------------------------------->" + str(trueFalse)
                        if(trueFalse == True):
                            print "WAZAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
                        if(trueFalse == False):
                            print "No trigger..."
                            
                        del queryManager.mainResult
                        queryManager.mainResult = list(queryManager.tmpMainResult)
            else:
                print "logfile has not changed"
            
            del queryManager.tmpMainResult
            del queryManager.mainResult
            queryManager.startAt = self.endPoint
            print "startat 3 " + str(queryManager.startAt)
            print "-----> 03 " + str(len(queryManager.mainResult))
            print "-----> 03 " + str(len(queryManager.tmpMainResult))
            time.sleep(10)
            logFile = fm.read(configuration.firewallLog)
            queryManager.mainResult = logFile
            queryManager.tmpMainResult = list(queryManager.mainResult)
            print "startat 4 " + str(queryManager.startAt)
            print str(len(logFile))
            print str(len(queryManager.mainResult))
            self.endPoint = len(logFile)
            print "-----> 04 " + str(len(queryManager.mainResult))
            print "-----> 04 " + str(len(queryManager.tmpMainResult))