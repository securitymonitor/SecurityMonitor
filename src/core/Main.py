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
    monitor.startMonitoring()
    monitor.endMonitoring()
    

if __name__ == '__main__':
    Main()