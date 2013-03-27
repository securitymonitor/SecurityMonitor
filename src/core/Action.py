class Action:

    def checkEntryFrequency(self, connection):
        import re

        print "$$connection = lnsplit() as variable 'connection' received: ", connection #debug
        fwFile = open("firewall.log")
        trafficList = []
        uniqueIPList = []
        maxIPconn = 50
        maxTimeThreshold = 60

        print "$$Append entries to list...$$"
        for fwEntry in fwFile.readlines():
            fwEntryMatchObj = re.search(connection, fwEntry)
            timeRegEx = re.search("(\w+\s\d+\s\d+:\d+:\d+)", fwEntry)
            #fwEntryMatchObj.group(1) + " " + 
            trafficList.append(fwEntryMatchObj.group(1))

            if fwEntryMatchObj.group(1) in uniqueIPList:
                #print "Already in list"
                #time.sleep(0.01)
                continue
            if fwEntryMatchObj.group(1) != uniqueIPList:            
                uniqueIPList.append(fwEntryMatchObj.group(1))
                print timeRegEx.group(1)


        for uniqueIP in uniqueIPList:
            print "$$Counting connection...$$", uniqueIP
            searchIPRegEx = "(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$)"
            uniqueIPMatchObj = re.search(searchIPRegEx, uniqueIP)
    
            for trafficEntry in trafficList:

                a = trafficList.count(uniqueIPMatchObj.group(1))
                continue
            print a
        fwFile.close()
        


    


