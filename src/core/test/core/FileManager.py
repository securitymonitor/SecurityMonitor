class FileManager:
       
    def get_rules(self):
        # Get all the available rules
        from Rules import Rules
        Rules = Rules()
        rule_files = Rules.get_rules()       
        return rule_files

    def get_ruledef(self):
        # Get the rule definitions which will be combined with the rule values for matching
        from Rules import Rules
        Rules = Rules()
        ruledef = Rules.get_ruledef()
        return ruledef
    
    def read_logfile(self, log_file):
        # The filename needs to be changed. The logfile location will be in the Rule.
        filename = log_file
        loglines = []
        read = open(filename, 'r')
        for _line in read:
            _line = _line.strip()
            loglines.append(_line)
        read.close()
        return loglines