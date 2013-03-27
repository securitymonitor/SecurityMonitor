'''
Created on Mar 6, 2013

@author: Sujen
'''

class FileManager:
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''
    def read(self, dirFile):
        file = open(dirFile)
        fileLines = file.readlines()
        file.close()
        return fileLines
    
    def write(self, dirFile, textData):
        file = open(dirFile, "r+")
        existingText = file.read()
        #file.seek(0)
        file.truncate()
        file.write(existingText + "\n" + textData) 
    
    def overwrite(self, regexList, file):
        file.truncate()
        for i in range(0, len(regexList)):
            file.write(regexList[i])  
        
    def exception(self, msg):
        dirError = "errorLog.txt"

        if(msg == ""):
            msg = "This is a default error..."
        
        fileManager = FileManager();
        fileManager.write(dirError, msg)        
        print "Error occured, see \"" + str(dirError) + "\" for further details..."
        
        
        