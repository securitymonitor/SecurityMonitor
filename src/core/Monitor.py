'''
Created on Mar 6, 2013

@author: vinesh
'''
from core.FileManager import FileManager

class Monitor:
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
    def startMonitoring(self):
        print "loading File Manager..."
        fileManager = FileManager()
        fileManager.read()
        print "Monitoring Started!"
        
    def endMonitoring(self):
        print "Monitoring Ended!"