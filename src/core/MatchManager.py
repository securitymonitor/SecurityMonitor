import re

class Matching:
    
    """
    This class is used to create the matchlist and combine it with the matching keywords in the RuleDefinitionsFile.txt
    
    matchlist =        The matchlist that is used for the actual matching of the logfile
    matchlist_keys=    An temporary dictionary that is used to get the value of the keys
    """
    
    matchlist = []
    matchlist_keys = {}
    
    def __init__(self, rule, ruledef):
        self.rule = rule
        self.ruledef = ruledef
        self.get_matches()
        self.get_matching_definitions()
    
    
    """
    This function is used to get all the keys matching the value of the MATCH key in the rule.
    """
    def get_matches(self):
        temp_matchlist = []

        #find the MATCH keyword in the rule file
        for keys in self.rule:
            match = re.findall('MATCH', keys)
            if match:
                matches = self.rule.get(keys)
                matches = matches.replace(" ", "")
                temp_matchlist = matches.split(",")
                        
        # find the matching values of the match keyword with the keywords in the file    
        matchlist_keys = {}
        for keys in self.rule:
            for line in range (len(temp_matchlist)):
                regex = temp_matchlist[line]
                match = re.findall(regex, keys)
                if match:
                    matches = self.rule.get(keys)
                    matchlist_keys.update({keys:matches})            
        
        # If a value in the rule has the same value as a name of a key.
        for key in matchlist_keys:
            for _x in self.rule:
                _y = _x.replace(' =', "")
                matchlist_keys[key] = matchlist_keys[key].replace(" ", "")
                if matchlist_keys.get(key) == _y:
                    matchlist_keys[key] = self.rule.get(_x)
        
        #Checks if the matchlist contains an *. If so, the key will be deleted.
        matchlist_keys = self.asterisk_check(matchlist_keys)
        self.matchlist_keys = matchlist_keys
                            
    
    """
    This function is used to combine the values of the matchlist with the values in the ruledef.
    """
    def get_matching_definitions(self):
        # match the keywords key and value            
        temp_list = []
        for line in self.matchlist_keys:
            for keys in self.ruledef:
                if line == keys[:-1]:     #Get rid of the whitespace at the end :)
                    matchlist_value = self.matchlist_keys.get(line)
                    ruledef_value = self.ruledef.get(keys)
                    temp_list = (ruledef_value, matchlist_value)
                    string = ', '.join(temp_list)
                    string = string.replace (',', '').replace(" ", "")
                    self.matchlist_keys[line] = string         
                               
        # Put the values of the dictionary in an list. The list is used to search the logfile
        matchlist = []
        for keys in self.matchlist_keys:
            key = self.matchlist_keys.get(keys)
            matchlist.append(key)  
        
        self.matchlist = matchlist
        print 'matchlist: ', self.matchlist
    
    """
    THis function checks if a value of the matchlist has an asterisk, it will be removed.
    """
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