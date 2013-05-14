'''
Created on May 4, 2013

@author: vinesh
'''
from core.Configuration import Configuration

class SMI:
    '''
    The Security Monitoring Interface
    '''
    #Configuration interface test
    config = Configuration()
    print "test: " + config.fromaddr

    def __init__(self):
        '''
        Constructor
        '''
        #Configuration interface
        self.config = Configuration()
