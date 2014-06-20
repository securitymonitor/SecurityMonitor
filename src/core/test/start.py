import re, sys, subprocess, os

def read_logfile():
    filename = 'log.txt'
    loglines = []
    read = open(filename, 'r')
    for _line in read:
        _line = _line.strip()
        loglines.append(_line)
    read.close()
    return loglines

def get_rules():
    from rules import Rules
    Rules = Rules()
    rule_files = Rules.get_rules()
    #ruledef = Rules.get_ruledef()
    
    return rule_files

def manager():
    #Get the rule and logfiles
    log = read_logfile()
    rules = get_rules()
    
    
    matchlist = []
    for x in rules:
        #find the MATCH keyword in the rule file
        for keys in x:
            match = re.findall('MATCH', keys)
            if match:
                matches = x.get(keys)
                matches = matches.replace(" ", "")
                temp_matchlist = matches.split(",")
        
        # find the matching values of the match keyword with the keywords in the file    
        for keys in x:
            for line in range (len(temp_matchlist)):
                regex = temp_matchlist[line]
                match = re.findall(regex, keys)
                if match:
                    matches = x.get(keys)
                    matchlist.append(matches)
            
    matchlist = asterisk_check(matchlist, x)      
    matchlist, regex = build_regex(matchlist)
    regex_count = match_with_log(matchlist, regex, log)
    rule_count_value, count_operator = get_count_operator(regex_count, x)
    action = compare_count(rule_count_value, regex_count, count_operator)
    do_action(action, x)
    
def asterisk_check(matchlijst, dictionary):

    count = 0
    for _x in matchlijst:
        y = _x.lstrip()
        matchlijst[count] = y
        count+=1
    
    for _x in matchlijst:
        if _x == '*':
            matchlijst.remove(_x)
            

    return matchlijst   
   
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

def do_action(action, rule):
    
    if action == True:
    
        folder = 'actions\ '
        
        #get action from rule
        for x in rule:
            match = re.findall('ACTION', x)
            if match:            
                rule_action = rule.get(x)
        
        action_target = folder + rule_action
        action_target = action_target.replace(" ", "").replace("'", '')
                         
        print 'het pad is ', os.path.exists(action_target)
        print action_target
        subprocess.call([sys.executable, action_target])

    else:
        pass
    
    
manager()



