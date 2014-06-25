from os import listdir, path
import re
from Configuration import Configuration

class Rules:
    
    def get_rules(self):
        config = Configuration()
        ruleDir = config.ruleDir
        
        regex = re.compile(".+=|.+<|.+>|.+<=|.+>=")
        #Rules worden uitgelezen
        print "Searching for rule files..."
        #ruleDir = 'rules/'   
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
                        filelist.update({match:y})
                contents.append(filelist)
                file.close()
        return contents
    
    
    def get_ruledef(self):
        config = Configuration()
        ruleDir = config.ruleDir
        print ruleDir 
        
        print "Searching for Rule Definition file"
        DefFile = ruleDir + 'RuleDefinitionTable.txt'
        print DefFile, 'found!'
        
        file = open(DefFile, 'r')
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
        