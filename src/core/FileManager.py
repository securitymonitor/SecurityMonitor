'''
Created on Mar 6, 2013

@author: vinesh
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
        file.seek(0)
        file.write(existingText + "\n" + textData)   
        
    def exception(self, msg):
        dirError = "errorLog.txt"

        if(msg == ""):
            msg = "This is a default error..."
        
        fileManager = FileManager();
        fileManager.write(dirError, msg)        
        print "Error occured, see \"" + str(dirError) + "\" for further details..."
        
        
        