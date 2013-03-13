'''
Created on Mar 6, 2013

@author: vinesh
'''
from core.Configuration import Configuration
from core.Monitor import Monitor

def Main():
    config = Configuration()
    monitor = Monitor()
    
    print "Starting program..."
    config.configure()
    dirConfig = config.rule
    dirLog = config.filename
    startAt = 0
    print "loading File Manager..."
    print "Monitoring Started!"
    monitor.startMonitoring(dirConfig,dirLog,startAt)
    #monitor.endMonitoring()
    

if __name__ == '__main__':
    Main()