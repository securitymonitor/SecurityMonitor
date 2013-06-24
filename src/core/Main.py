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
    dirConfig = config.ruleFiles
    #config.rule
    dirLog = "TestFirewall.log"
    #config.filename
    print "loading File Manager..."
    print "Monitoring Started!"

    
    daemon = threading.Thread(name='Main Daemon Thread', target=monitor.testMonitoring())
    daemon.setDaemon(True)
    daemon.start()
    
    #monitor.endMonitoring()

if __name__ == '__main__':
    Main()