import re

class Matching:
    
    def get_matches(self, log, rule):
        temp_matchlist = []
        matchlist_keys = {}
        
        #find the MATCH keyword in the rule file
        for keys in rule:
            match = re.findall('MATCH', keys)
            if match:
                matches = rule.get(keys)
                matches = matches.replace(" ", "")
                temp_matchlist = matches.split(",")
                        
        # find the matching values of the match keyword with the keywords in the file    
        for keys in rule:
            for line in range (len(temp_matchlist)):
                regex = temp_matchlist[line]
                match = re.findall(regex, keys)
                if match:
                    matches = rule.get(keys)
                    matchlist_keys.update({keys:matches})            
        
        matchlist_keys = self.asterisk_check(matchlist_keys)
        
        return matchlist_keys
                            
    def get_matching_definitions(self, matchlist_keys, ruledef):
        # match the keywords key and value            
        temp_list = []
        for line in matchlist_keys:
            for keys in ruledef:
                if line == keys[:-1]:     #Get rid of the whitespace at the end :)
                    matchlist_value = matchlist_keys.get(line)
                    ruledef_value = ruledef.get(keys)
                    temp_list = (ruledef_value, matchlist_value)
                    string = ', '.join(temp_list)
                    string = string.replace (',', '').replace(" ", "")
                    matchlist_keys[line] = string         
                               
        # Put the values of the dictionary in an list. The list is used to search the logfile
        matchlist = []
        for keys in matchlist_keys:
            key = matchlist_keys.get(keys)
            matchlist.append(key)  
        
        print 'matchlist: ', matchlist
        return matchlist
        
        
    def asterisk_check(self, matchlist):  
        temp_matchlijst = {}
           
        count = 0
        for _x in matchlist:
            y = matchlist.get(_x).lstrip()
            temp_matchlijst.update({_x:y})
            count+=1
        
        matchlist = temp_matchlijst
        temp_matchlijst = {}
         
        for _x in matchlist:
            if matchlist.get(_x) == '*':
                pass
            else:
                y = matchlist.get(_x)
                temp_matchlijst.update({_x:y})
           
        return temp_matchlijst    
    