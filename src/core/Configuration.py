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
    FirewallLog = "TestFirewall.log"
    RuleDefinitionTable = "RuleDefinitionTable.txt"
    exceptionFile = "errorLog.txt"
    fromaddrs = ""
    toaddrs = ""
    username = ""
    password = ""
    server = ""
    LogDir = ""
    RuleDir = ""
    
    def __init__(self):
        '''
        Constructor
        '''
        self.configure()
    
    def configure(self):
        print"Configuring..."
        #configuration example code here
     
        fm = FileManager()
        allLines = fm.read("Config.txt")
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
            if 'LogDir' in data:
                self.LogDir = str(data[1])
            if 'RuleDir' in data:
                self.RuleDir = str(data[1])
                    
       
        try:
            filename = self.LogDir
            
        #Set the filename and open the file
        #filename = 'log.txt' #nog aangepast worden naar formulier input
            fm.read(filename)

#does the file exists
        except IOError as e:
            print "Log " + filename + " bestaat niet".format(e.errno, e.strerror)


        else:
            print " Log " + filename + " geselecteerd "
        #find end of file
   
        
    #rule definieren     Werkt wel   
        try:
        #Set the rule to use
            rule = self.RuleDir #nog aangepast worden naar formulier input
            file = execfile(rule)
            
            

#does the file exists
        except IOError as e:
            print "Rule " + rule + " bestaat niet".format(e.errno, e.strerror)
            
        else:
            print " Ruleset " + rule + " is ingeladen"
        
        print "Configuration completed."
        