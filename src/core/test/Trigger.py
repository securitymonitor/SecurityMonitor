import subprocess
import re
import os
import sys

class Trigger():
    
    def perform_action(self,action, rule):
        if action == True:
    
            folder = 'actions\ '
            #get action from rule
            for x in rule:
                match = re.findall('ACTION', x)
                if match:            
                    rule_action = rule.get(x)
            
            action_target = folder + rule_action
            action_target = action_target.replace(" ", "").replace("'", '')
                             
            if os.path.exists(action_target) is True:
                print 'The action rule is : ', action_target
                subprocess.call([sys.executable, action_target, rule])
            else:
                print 'The action rule is not valid. Please use the correct path of the file.'
            
        else:
            # There is no action needed.
            pass