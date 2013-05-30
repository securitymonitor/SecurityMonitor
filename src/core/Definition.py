class Definitions:

    ACTION,COUNT,DATA,DESCRIPTION,NAME,SOURCEIP,SOURCEPT,TARGETIP,TARGETPT,TIME = range(10)
    
    @classmethod
    def toString(self, val):
        for k,v in vars(self).iteritems():
            if v==val:
                return k        
    @classmethod
    def readConfigFile(self):
        configFile = open("RuleDefinitionTable.txt")
        configFileRead = configFile.readlines()
        valueAssignment = "="
        valDict = {}

        for confLine in configFileRead:
            confLine = confLine.strip()
            if valueAssignment in confLine:
                keyword, value = confLine.split(valueAssignment, 1)
                keyword = keyword.strip()
                value = value.strip()

                valDict[keyword] = value
        configFile.close()
        return valDict

    @classmethod
    def getValueDefinition(self, str):
        tempDict = Definitions.readConfigFile()
        b = ''
        if tempDict.has_key(str):
            b = tempDict.get(str).replace("'", "")

        return b

Definitions.ACTION      = ''
Definitions.COUNT       = ''
Definitions.DATA        = ''
Definitions.DESCRIPTION = ''
Definitions.NAME        = ''
Definitions.SOURCEIP    = ''
Definitions.SOURCEPT    = ''
Definitions.TARGETIP    = ''
Definitions.TARGETPT    = ''
Definitions.TIME        = ''


a = Definitions.getValueDefinition('SOURCEIP')
print a

#print Definitions.toString(2)

#for k,v in sorted(b.items()):
#    print k, '=', v


