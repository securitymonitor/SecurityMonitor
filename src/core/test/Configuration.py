import re

class Configuration():
    configFile = ""
    fromaddr = ""
    toaddr = ""
    username = ""
    password = ""
    server = ""
    ruleDir = ""
    actionDir = ""
    interval = 0
    sleeptimer = ""

    def __init__(self):
        '''
        Constructor
        '''
        self.auto_configuration()
        
    def manual_configuration(self):
        configfile = 'Config.txt'
    
        return configfile
   
    def auto_configuration(self):
        configlist = self.read_configuration_file()
        
        self.ruleDir =  configlist['ruleDir']
        self.actionDir = configlist['actionDir']
        self.interval = configlist['interval']
        
        self.fromaddr = configlist['fromaddr']
        self.toaddr  =  configlist['toaddr']
        self.username = configlist['username']
        self.password = configlist['password']
        self.server   = configlist['server']
        
        self.sleeptimer = configlist['sleeptimer']
      
    def read_configuration_file(self):
        configfile = self.manual_configuration()
                    
        file = open(configfile, 'r')
        
        configlist = {}
        regex = '.+ = .*?'
        for line in file:
            match = re.findall(regex, line)
            if match:
                match = ''.join(match)
                x,y = line.split(match)
                y = y.strip('\n')
                y = y.strip(" ' ").strip('')
                match = match.replace(" ", '')           
                configlist.update({match:y})
        
        return configlist
        