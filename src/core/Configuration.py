'''
Created on Mar 6, 2013

@author: Dave
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
        print"Configuring..."
        #configuration example code here
        rule1 = Rule()
        rule1.test()
        
         
    try:
        #Set the filename and open the file
        filename = 'log.txt' #nog aangepast worden naar formulier input
        

#does the file exists
    except IOError as e:
        print "Log " + filename + " bestaat niet".format(e.errno, e.strerror)


    else:
        print " Log " + filename + " geselecteerd"
        #find end of file
   
        
    #rule definieren     Werkt wel   
        try:
        #Set the rule to use
            rule = 'rule1.py' #nog aangepast worden naar formulier input
            file = execfile(rule)
            
            

#does the file exists
        except IOError as e:
            print "Rule " + rule + " bestaat niet".format(e.errno, e.strerror)
            
        else:
            print " Ruleset " + rule + " is ingeladen"
        
        print "Configuration completed."