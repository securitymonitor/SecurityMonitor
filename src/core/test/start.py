import re



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

def producer():
    log = read_logfile()
    rules = get_rules()
    
    important = ['SOURCEIP = , TARGETIP = , PROTOCOL = ']
    lijst = []
    
    for x in rules:
        for keys in x:
            print keys
            if keys == 'SOURCEIP =' or keys == 'TARGETIP =' or keys == 'PROTOCOL =' or keys == 'MESSAGE =':
                lijst.append(x[keys])
    
    return lijst, x        
        #for x in _x.values():
            #print x
    
def asterisk_check():

    matchlijst, dictionary = producer()

    count = 0
    for _x in matchlijst:
        y = _x.lstrip()
        matchlijst[count] = y
        count+=1
    
    for _x in matchlijst:
        if _x == '*':
            matchlijst.remove(_x)
            print _x

    return matchlijst   
   
   
def match_log():
    matchlijst = asterisk_check()
    log = read_logfile()
    
    for _x in matchlijst:
        regex = _x
        for line in log:
            match = re.findall('145.92.6.10|UDP', line)
            if match: 
                print match 
   
   
match_log()



