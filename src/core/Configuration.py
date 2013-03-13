'''
Created on Mar 6, 2013

@author: vinesh
'''
from core.Rule import Rule

class Configuration:
    '''
    classdocs
    '''
    
    
    def __init__(self):
        '''
        Constructor
        '''
    
    def configure(self):
        print "Configuring..."
        #configuration example code here
        rule1 = Rule()
        rule1.test()
        print "Configuration completed."