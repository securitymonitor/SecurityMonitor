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
   
def build_regex():
    matchlijst = asterisk_check()

    
    regex = ''
    temp = []
    for _x in range(len(matchlijst)):
        match = re.findall('(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', matchlijst[_x])
        if match:
            for char in matchlijst[_x]:
                if char is '.':
                    print 'char = ' + str(char)
                    char = char.replace('.','[.]')
                    temp.append(char)
                else:
                    temp.append(char)
            char = ''.join(temp)
            matchlijst [_x] = char
        
        regex = regex +"(?=.*"+ str(matchlijst[_x]) +')'
    
    return matchlijst, regex

def match_with_log():
    log = read_logfile()   
    matchlijst, regex = build_regex()
             
    for line in log:
        match = re.findall(regex, line)
        if match:
            print 'regex = ' + str(regex) + "  line = " + str(line)
            pass 
            #print match 
   
   
match_with_log()



