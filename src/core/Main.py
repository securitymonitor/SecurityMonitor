'''
Created on Mar 6, 2013

@author: vinesh
'''
from core.Configuration import Configuration
from core.Monitor import Monitor
from core.Rule import Rule

def Main():
    config = Configuration()
    monitor = Monitor()
    rule = Rule()
    
    print "Starting program..."
    config.configure()
    dirConfig = "TestRules.txt"
    #config.rule
    dirLog = "TestFirewall.log"
    #config.filename
    startAt = 0
    print "loading File Manager..."
    print "Monitoring Started!"

    monitor.startMonitoring(dirConfig,dirLog,startAt)
    #monitor.endMonitoring()

if __name__ == '__main__':
    Main()