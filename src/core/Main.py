'''
Created on Mar 6, 2013

@author: vinesh
'''
from core.Configuration import Configuration
from core.Monitor import Monitor
from core.Rule import Rule
import threading

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

    
    t = threading.Thread(target=monitor.startMonitoring(dirConfig,dirLog,startAt))
    t.setDaemon(True)
    t.start()
    
    #monitor.endMonitoring()

if __name__ == '__main__':
    Main()