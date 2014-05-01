
# Installation script for Config.txt

class Installation:
    choice = raw_input("Do you want to configure SecMon? (y/n) ")
    choice = choice.lower()
    
    if choice == 'yes' or choice == 'y':
        print "Configuring the configuration file "
        
        LogDir_input = raw_input("Path to firewall log: Default: (../core/) : ")
        if LogDir_input == "":
            LogDir_input = '../core/'
        LogDir = "logDir = " + str(LogDir_input)
        
        RuleDir_input = raw_input ("Path to rule files: Default: (../custom/rules/) :")
        if RuleDir_input == "":
            RuleDir_input = '../custom/rules/'
        RuleDir = 'ruleDir = ' + str(RuleDir_input)
        
        ActionDir_input = raw_input ("Path to action files: Default: (../custom/actions/) :")
        if ActionDir_input == "":
            ActionDir_input = '../custom/actions/'
        ActionDir = 'actionDir = ' + str(ActionDir_input)
        
        Interval_input = raw_input ("Interval: Default: (30) :")
        if Interval_input == "":
            Interval_input = '30'
        Interval = 'interval = ' + str(Interval_input)
        
        fromaddr_input = raw_input ("Email address of the sender: Example: sendfrom@example.com :")
        fromaddr = 'fromaddr = ' + str(fromaddr_input)
        toaddr_input = raw_input ("Email address of the recipient: Example: sento@example.com : ")
        toaddr = 'toaddr = ' + str(toaddr_input)
        server_input = raw_input("SMTP server: Example: smtp.server.com:25 :")
        server = 'server = ' + str(server_input)
        ask = raw_input ("Does the smtp server (" + str(server_input) + ") require a username and password? (y/n) ")
        ask = ask.lower()
        
        if ask == 'yes' or ask == 'y':
            username_input = raw_input("Username: ")
            password_input = raw_input ("Password: ")
            username = 'username = ' + str(username_input)
            password = 'password = ' + str(password_input)
        else:
            username = 'username = '
            password = 'password = '
                
        #write the input to the configuration file
        try:
            file = open ('Config.txt', 'w')
            file.write ("//directories of the Files:\n")
            file.write (str(LogDir) + "\n")
            file.write (str(RuleDir) + "\n")
            file.write (str(ActionDir) + "\n")
            file.write (str(Interval) + "\n")
            file.write ("\n")        
            file.write (str(fromaddr) + "\n")
            file.write (str(toaddr) + "\n")
            file.write (str(username) + "\n")
            file.write (str(password) + "\n")
            file.write (str(server) + "\n")    
            print "Done writing to Config.txt"
        except:
            print 'Error writing to Config.txt'
            
    else:
        print 'Ok. Abort!'