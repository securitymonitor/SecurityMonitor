import re, sys, subprocess, os
from threading import Thread

def log_check(rule):
    #Checks the passed rule for the LOG keyword for which logfile to use
    log_files = []
    for keys in rule:
        match = re.findall('LOG', keys)
        if match:
            matches = rule.get(keys)
            matches = matches.replace(" ", "")
            log_files.append(matches)
    
    # The list is used to use more than one log file per rule, however this is not yet implemented in the rest of the code.
    if len(log_files) == 1:
        return log_files[0]
    else:
        print 'Error with the logfile. Please check the value of the LOG keyword in the rule file'

def Monitor():
    from FileManager import FileManager
    FileManager = FileManager()
    rules = FileManager.get_rules()
    ruledef = FileManager.get_ruledef()

    for rule in range (len(rules)):
        thread = Thread( target=manager, args=(rules[rule], ruledef))
        thread.start() 

def manager(rule, ruledef):
    from Matching import Matching
    Matching = Matching()
    
    log = log_check(rule)
    temp_matchlist = Matching.get_matches(log, rule)
    matchlist = Matching.get_matching_definitions(temp_matchlist, ruledef)
           
    #matchlist = asterisk_check(matchlist, rule)  
    matchlist, regex = build_regex(matchlist)
    regex_count = match_with_log(matchlist, regex, log)
    rule_count_value, count_operator = get_count_operator(regex_count, rule)
    action = compare_count(rule_count_value, regex_count, count_operator)
    perform_action(action, rule)
       
def build_regex(matchlijst):

    regex = ''
    temp = []
    for _x in range(len(matchlijst)):
        match = re.findall('(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', matchlijst[_x])
        if match:
            for char in matchlijst[_x]:
                if char is '.':
                    #print 'char = ' + str(char)
                    char = char.replace('.','[.]')
                    temp.append(char)
                else:
                    temp.append(char)
            char = ''.join(temp)
            matchlijst [_x] = char
        
        regex = regex +"(?=.*"+ str(matchlijst[_x]) +')'
    
    return matchlijst, regex

def match_with_log(matchlijst, regex, log):
    
    regex_count = 0         
    for line in log:
        match = re.findall(regex, line)
        if match:
            #print 'regex = ' + str(regex) + "  line = " + str(line)
            regex_count+=1
    return regex_count

def get_count_operator(regex_count, rule):
   
    for x in rule:
        match = re.findall('COUNT', x)
        if match:
            rule_count_value = rule.get(x)
            rule_count_value = rule_count_value.replace(" ", "")
            rule_count_value = int (rule_count_value)
            rule_count = x
    
    count_operator = rule_count[-2:]
    count_operator = count_operator.replace(" ", "")
    
    return rule_count_value, count_operator    

def compare_count(rule_count_value, regex_count, count_operator):
    
    action = False
    if count_operator == '=':
        print regex_count, type(regex_count)
        print rule_count_value , type (rule_count_value)
        if regex_count == rule_count_value:
            action = True
    if count_operator == '<':
        if regex_count < rule_count_value:
            action = True
    if count_operator == '>':
        if regex_count > rule_count_value:
            action = True
    if count_operator == '<=':
        if regex_count <= rule_count_value:
            action = True
    if count_operator == '>=':
        if regex_count >= rule_count_value:
            action = True 
    
    return action

def perform_action(action, rule):
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
            subprocess.call([sys.executable, action_target])
        else:
            print 'The action rule is not valid. Please use the correct path of the file.'
        
    else:
        # There is no action needed.
        pass
    
Monitor()
