class FileManager:
    
    """
    This class is used to get the rules, get the rule definitions and to read the log files.
    """
    
    """
    This function is used to get all the available rules in the ruleDir.
    """
    def get_rules(self):
        from Rules import Rules
        Rules = Rules()
        rule_files = Rules.get_rules()       
        return rule_files
    
    """
    This function is used to get the rule definitions.
    """
    def get_ruledef(self):
        from Rules import Rules
        Rules = Rules()
        ruledef = Rules.get_ruledef()
        return ruledef
    
    """
    This function is used to read the logfile
    """
    def read_logfile(self, log_file):
        filename = log_file
        loglines = []
        read = open(filename, 'r')
        for _line in read:
            _line = _line.strip()
            loglines.append(_line)
        read.close()
        return loglines