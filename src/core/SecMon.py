'''
Created on 14 mei 2013

@author: Sujen
'''

import sys
import re
from FileManager import FileManager
from core.Configuration import Configuration

class SecMon:
    '''
    SecMon:
        This class can be called to edit a value for a keyword in a rule file using command lines.
        
        configuration         = Instance of the Configuration class.
        dirConfig             = Directory of the config file.
        fileManager           = Instance of the FileManager class.
        configLines           = List of each line in a config file.
        listKeywords          = Keywords defined in a config file.
    '''
    configuration = Configuration()
    dirConfig = configuration.configFile
    fileManager = FileManager()
    configLines = fileManager.read(dirConfig)
    listKeywords = ["fromaddr","toaddrs","username","password","server"]
    
    if(str(sys.argv[1]) == "-h"):
        print "The right format for the configure command is: \nSecMon.py <Argument> <newValue>\n"
        print "If you want to know what arguments are available see below:"
        
        for i in range(0,len(listKeywords)):
            print listKeywords[i]
    
    for i in range(0,len(configLines)):
        if(re.search(str(sys.argv[1]), configLines[i])):
            configLines[i] = str(sys.argv[1])+" = "+ str(sys.argv[2])+"\n" 
            fileManager.overwrite(configLines, dirConfig)