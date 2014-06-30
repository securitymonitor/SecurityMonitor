import re

class Configuration():   
    
    """
    This class contains the general configuration values of the application.
     
    configfile =     Name of the configuration file
    fromaddr =       The email-adress of the sender.
    toaddr =         The email-adress of the receiver.
    username =       The username of the email-account.
    password =       The password of the email-account.
    server =         The server name of the SMPT-server.
    ruleDir =        Directory of the rule file.
    actionDir =      Directory of the action file.
    interval =       The sleep time in the monitor for each rule
    """
    
    
    def __init__(self):
        self.auto_configuration()
    
    """
    This function is used for the configuration that has to be added manually.
    """
    def manual_configuration(self):
        configfile = 'Config.txt'
        return configfile
   
    """
    This function sets the variables to the values given in the config file.
    """
    def auto_configuration(self):
        configlist = self.read_configuration_file()
        
        self.ruleDir =  configlist['ruleDir=']
        self.actionDir = configlist['actionDir=']
        self.interval = configlist['interval=']
        
        self.fromaddr = configlist['fromaddr=']
        self.toaddr =  configlist['toaddr=']
        self.username = configlist['username=']
        self.password = configlist['password=']
        self.server = configlist['server=']
        
        self.sleeptimer = configlist['sleeptimer=']
    
    
    """
    This function is used to read the configuration file and put everything in a dictionary.
    """  
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
        