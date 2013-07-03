'''
Created on Mar 6, 2013

@author: Dave
'''
#from core.Rule import Rule
from core.FileManager import FileManager

class Configuration:
    '''
    classdocs
    '''
    configFile = "Config.txt"
    firewallLog = "TestFirewall.log"
    ruleDefinitionTable = "..\\custom\\rules\\RuleDefinitionTable.txt"
    ruleFiles = []
    actionFiles = []
    exceptionFile = "errorLog.txt"
    fromaddrs = ""
    toaddrs = ""
    username = ""
    password = ""
    server = ""
    logDir = ""
    ruleDir = ""
    actionDir = ""
    interval = 0
    
    def __init__(self):
        '''
        Constructor
        '''
        self.configure()
    
    @classmethod
    def getRuleFiles(self, ruleDir):
        print "Searching for rule files..."
        from os import listdir
        import re
        del self.ruleFiles[:]
        ruleFiles = listdir(ruleDir)
        ruleFilePattern = re.compile('rule.+?.txt')
        for file in ruleFiles:
            fileMatch = re.match(ruleFilePattern, file)
            if fileMatch:
                self.ruleFiles.append(file) 
    
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
                    
    def configure(self):
        print"Configuring..."
        #configuration example code here
     
        fm = FileManager()
        allLines = fm.read(self.configFile)
        for line in allLines:
            data = [x.strip() for x in line.split('= ')]
            if 'fromaddr' in data:
                self.fromaddr = str(data[1])
            if 'toaddrs' in data:
                # put data into string
                self.toaddrs = str(data[1])
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
       
        try:
            filename = self.logDir
            
        #Set the filename and open the file
        #filename = 'log.txt' #nog aangepast worden naar formulier input
            fm.read(filename)
        #does the file exists
        except IOError as e:
            print ""
        #print "Log " + filename + " bestaat niet".format(e.errno, e.strerror)

        else:
            print " Log " + filename + " geselecteerd "
        #find end of file
        
        #rule definieren     Werkt wel   
        try:
        #Set the rule to use
            rule = self.ruleDir #nog aangepast worden naar formulier input
            file = execfile(rule)

        #does the file exists
        except IOError as e:
        #print "Rule " + rule + " bestaat niet".format(e.errno, e.strerror)
            print ""
            
        else:
            print " Ruleset " + rule + " is ingeladen"
            
        print "Configuration completed."
        