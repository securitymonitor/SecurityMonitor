'''
Created on Mar 6, 2013

@author: vinesh
'''

from core.Configuration import Configuration
from core.Monitor import Monitor
from core.Rule import Rule
from threading import Thread

def Main():
    config = Configuration()
    monitor = Monitor()

    print "Starting program..."
    config.configure()
    print "loading File Manager..."
    print "Monitoring Started!"
    
    daemon = Thread(name='Main Daemon Thread', target=monitor.testMonitoring())
    daemon.setDaemon(True)
    daemon.start()

if __name__ == '__main__':
    Main()