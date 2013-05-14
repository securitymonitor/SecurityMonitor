'''
Created on 14 mei 2013

@author: Sujen
'''

import sys
import re
from FileManager import FileManager

class SecMon:
    dirConfig = "Config.txt"
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