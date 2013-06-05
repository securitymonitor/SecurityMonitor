'''
Created on Mar 6, 2013

@author: vinesh
'''
                                            #-----------------------------------|
#import os, sys                             #<---------|Nodig voor op de server.|
#sys.path.append("//home//jasper//src//")   #<----------------------------------|
from core.Configuration import Configuration
from core.Monitor import Monitor
from core.Rule import Rule
import threading


def Main():
    config = Configuration()
    monitor = Monitor()
    rule = Rule()
    
    print "Starting program..."
    config.configure()
    dirConfig = config.ruleFile
    #config.rule
    dirLog = "TestFirewall.log"
    #config.filename
    startAt = 0
    print "loading File Manager..."
    print "Monitoring Started!"

    
    t = threading.Thread(target=monitor.testMonitoring(dirConfig,dirLog,startAt))
    t.setDaemon(True)
    t.start()
    
    #monitor.endMonitoring()

if __name__ == '__main__':
    Main()
#
#------------------------------------------------------------------------------------------------------
#'''
#Created on Mar 6, 2013

#@author: vinesh
#'''
#import os, sys
#sys.path.append("//home//jasper//src//")
#from core.Configuration import Configuration
#from core.Monitor import Monitor
#from core.Rule import Rule
#import threading

#def Main():
#    print "in Main"
#    config = Configuration()
#    monitor = Monitor()
#    rule = Rule()   
    
#    print "Starting program..."
#    config.configure()
#    dirConfig = "TestRules.txt"
#    #config.rule
#    dirLog = "TestFirewall.log"
#    #config.filename
#    startAt = 0
#    print "loading File Manager..."
#    print "Monitoring Started!"

#    monitor.testMonitoring(dirConfig,dirLog,startAt)
#    #t = threading.Thread(target=monitor.testMonitoring(dirConfig,dirLog,startAt))
#    #t.setDaemon(True)
#    #t.start()
    
#    #monitor.endMonitoring()

#if __name__ == '__main__':
#    try:
#        pid = os.fork()
#        print "1"
#        if pid > 0:
#            print "6ex"
#            sys.exit(0)
#    except OSError, e:
#        print >>sys.stderr, "fork #1 failed: %d (%s)" % (e.errno, e.strerror)
#        sys.exit(1)

#    #os.chdir("//home//jasper//src//")
#    os.setsid()
#    os.umask(0)

#    try:
#        pid = os.fork()
#        if pid > 0:
#            print "Daemon PID %d" % pid
#            sys.exit(0)
#    except OSError, e:
#        print >>sys.stderr, "fork #2 failed: %d (%s)" % (e.errno, e.strerror)
#        sys.exit(1)
#    Main()