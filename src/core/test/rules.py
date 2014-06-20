from os import listdir, path
import re

class Rules:
    
    def get_rules(self):
        regex = re.compile(".+=|.+<|.+>|.+<=|.+>=")
        #Rules worden uitgelezen
        print "Searching for rule files..."
        ruleDir = 'rules/'
            
        if path.isdir(ruleDir) is True: # checks if the given path exists
            DirFiles = listdir(ruleDir)
        
        contents = []
        for line in DirFiles:
            fileDir = ruleDir + line
            print line
            if line == 'RuleDefinitionTable.txt':
                pass
            else:
                file = open(fileDir, 'r')   
                filelist = {}
                for _line in file:
                    match = re.findall(regex, _line)
                    if match:
                        match = ''.join(match)
                        x,y = _line.split(match)
                        y = y.strip('\n')
                        y = y.strip('')
                        #contents.append(match)
                        filelist.update({match:y})
                        #print filelist
                contents.append(filelist)
                file.close()
        return contents
    
    
    def get_ruledef(self):
        print "Searching for Rule Definition file"
        DirFile = 'rules/RuleDefinitionTable.txt'
        
        file = open(DirFile, 'r')
        rulelist = {}
        regex = '.+ = .*?'
        for line in file:
            match = re.findall(regex, line)
            if match:
                match = ''.join(match)
                x,y = line.split(match)
                y = y.strip('\n')
                y = y.strip(" ' ").strip('')           
                rulelist.update({match:y})
        return rulelist
            
            
        
        
        
        