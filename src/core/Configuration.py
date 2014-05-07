'''
Created on Mar 6, 2013

@author: Dave
'''

import os
import sys
os.chdir('core')
from core.FileManager import FileManager

class Configuration:
    '''
    Configuration:
    This class contains the general configuration values of the application.
    
        configFile             = Name of the configuration file.
        firewallLog            = Name of the firewall file. 
        ruleDefinitionTable    = Path to the rule definition table file.
        ruleFiles              = List for all files in the rule directory.
        actionFiles            = List for all files in the action directory.
        exceptionFile          = Path to the exception file.
        fromaddr              = The email-adress of the sender.
        toaddr                = The email-adress of the receiver.  
        username               = The username of the email-account. 
        password               = The password of the email-account.  
        server                 = The server name of the SMPT-server.
        logDir                 = Directory of the log file.
        ruleDir                = Directory of the rule file. 
        actionDir              = Directory of the action file.   
        interval               = The sleep time in the monitor for each rule.
    '''
    
    configFile = "Config.txt"
    firewallLog = "TestFirewall.log"
    ruleDefinitionTable = "..//custom//rules//RuleDefinitionTable.txt"
    ruleFiles = []
    actionFiles = []
    exceptionFile = "errorLog.txt"
    fromaddr = ""
    toaddr = ""
    username = ""
    password = ""
    server = ""
    logDir = ""
    ruleDir = ""
    actionDir = ""
    interval = 0
    sleeptimer = ""
        
    '''
    This is the initialization function.
    This calls the configure function that initializes all variables.
    '''
    def __init__(self):
        '''
        Constructor
        '''
        self.configure()
    
    '''
    This function gets all files in the rule directory.
    '''
    @classmethod
    def getRuleFiles(self, ruleDir):
        print "Searching for rule files..."
        from os import listdir
        import re
        del self.ruleFiles[:]
        ruleFiles = listdir(ruleDir)
        ruleFilePattern = re.compile('.+?.*')
        for file in ruleFiles:
            fileMatch = re.match(ruleFilePattern, file)
            if fileMatch:
                self.ruleFiles.append(file) 
    
    '''
    This function gets all filenames in the action directory.
    '''
    @classmethod                
    def getActionNames(self, actionDir):
        from os import listdir
        import re
        del self.actionFiles[:]
        actionFiles = listdir(actionDir)
        actionFilePattern = re.compile('.+?.*')
        for file in actionFiles:
            fileMatch = re.match(actionFilePattern, file)
            if fileMatch:
                self.actionFiles.append(file) 
                print str(file)     
     
    '''
    This function sets the variables to the values given in the config file.
    '''               
    def configure(self):
        print"Configuring..."
        #configuration example code here
     
        fm = FileManager()
        allLines = fm.read(self.configFile)
        for line in allLines:
            data = [x.strip() for x in line.split('= ')]
            if 'sleeptimer' in data:
                self.sleeptimer = str(data[1])
            if 'fromaddr' in data:
                self.fromaddr = str(data[1])
            if 'toaddr' in data:
                # put data into string
                self.toaddr = str(data[1])
            if 'username' in data:
                # put data into string
                self.username = str(data[1])
            if 'password' in data:
                # put data into string
                self.password = str(data[1])
            if 'server' in data:
                # put data into string
                self.server = str(data[1])
            if 'logDir' in data:
                self.logDir = str(data[1])
            if 'ruleDir' in data:
                self.ruleDir = str(data[1])
                Configuration.getRuleFiles(self.ruleDir)
            if 'actionDir' in data:
                self.actionDir = str(data[1])
                Configuration.getActionNames(self.actionDir)
            if 'interval' in data:
                if(str(data[1]).__contains__(":")):
                    timeInterval = str(data[1]).split(":")
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
                    self.interval = int(str(data[1]))       
