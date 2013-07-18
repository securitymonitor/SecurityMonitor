'''
Created on Mar 6, 2013

@author: vinesh
'''
import sys
import os

os.getcwd()
os.chdir('..')
sys.path.append(os.getcwd())

from core.Configuration import Configuration
from core.Monitor import Monitor
from core.Rule import Rule
from threading import Thread

def Main():
    config = Configuration()
    monitor = Monitor()

    config.configure()
    
    daemon = Thread(name='Main Daemon Thread', target=monitor.startMonitoring())
    daemon.setDaemon(True)
    daemon.start()

if __name__ == '__main__':
    Main()
