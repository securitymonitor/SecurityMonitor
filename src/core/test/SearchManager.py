import re

class SearchManager():
    
    def __init__(self):
        self.logcounter()
    
    def searchmanager(self, matchlist, rule, log):
        matchlist, regex = self.build_regex(matchlist)
        regex_count = self.match_with_log(regex, log)
        rule_count_value, count_operator = self.get_count_operator(regex_count, rule)
        action = self.compare_count(rule_count_value, regex_count, count_operator)
        
        return action
        
    def build_regex(self,matchlist):
        regex = ''
        temp = []
        for _x in range(len(matchlist)):
            match = re.findall('(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', matchlist[_x])
            if match:
                for char in matchlist[_x]:
                    if char is '.':
                        #print 'char = ' + str(char)
                        char = char.replace('.','[.]')
                        temp.append(char)
                    else:
                        temp.append(char)
                char = ''.join(temp)
                matchlist [_x] = char
                
            regex = regex +"(?=.*"+ str(matchlist[_x]) +')'
            
        return matchlist, regex
    
    def match_with_log(self,regex, log):
        regex_count = 0         
        for line in log:
            match = re.findall(regex, line)
            if match:
                #print 'regex = ' + str(regex) + "  line = " + str(line)
                regex_count+=1
        return regex_count
    
    def get_count_operator(self, regex_count, rule):
       
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
    
    def compare_count(self, rule_count_value, regex_count, count_operator):

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
    
    def logcounter(self):
        self.endPoint = 0
        self.startAt = 0
        
        
    
        