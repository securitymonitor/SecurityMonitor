import subprocess
import re
import os
import sys
from Configuration import Configuration

class Trigger():
    
    """
    This class is used to perform an action in case of a trigger.
    """
    
    
    def perform_action(self,action, rule):
        if action == True:
            
            config = Configuration()
        
            folder = config.actionDir
            #get action from rule
            for x in rule:
                match = re.findall('ACTION', x)
                if match:            
                    rule_action = rule.get(x)
                    
            print 'Attack Detected!'
            
            actions = rule_action.split(',')
            for action in actions:
                action = action.replace("'","" ).replace(" ", '')
                
                action_target = folder + action
                action_target = action_target.replace(" ", "").replace("'", '')
                
                     
                if os.path.exists(action_target) is True:
                    #print 'The action rule is : ', action_target
                    subprocess.call([sys.executable, action_target, rule['DESCRIPTION =']])
                else:
                    print 'The action rule is not valid. Please use the correct path of the file.'
            
        else:
            print 'No Attack detected...'
            