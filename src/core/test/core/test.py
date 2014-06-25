
import re

def read_logfile():
    # The filename needs to be changed. The logfile location will be in the Rule.
    filename = 'log.txt'
    loglines = []
    read = open(filename, 'r')
    for _line in read:
        _line = _line.strip()
        loglines.append(_line)
    read.close()
    return loglines

def monitor():
    log = read_logfile()
    
    log_length = len(log)
    print log_length
    endpoint = log_length
        
def read_part_of_logfile():
    
    filename = 'log.txt'
    loglines = []
    read = open(filename, 'r')
    for _line in read:
        _line = _line.strip()
        loglines.append(_line)
    read.close()
    return loglines


def interval_check():
    
    interval = '10:30:10'
    
    interval_time = interval.split(":")
    print len(interval_time)
    
    if len(interval_time) == 3: # hours
        hour = int(interval_time[0])
        minutes = int(interval_time[1])
        seconds = int(interval_time[2])
        interval = hour*3600 + minutes*60 + seconds
        return interval
    elif len(interval_time) == 2: # minutes
        minutes = int(interval_time[0])
        seconds = int(interval_time[1])
        interval = minutes*60 + seconds    
        return interval
    elif len(interval_time) == 1:
        seconds = int (interval_time[0])
        interval = seconds
        return interval
    else:
        print ('Interval is incorrect')



    
def build_regex():
    matchlist = ['SRC=145.92.6.10', 'PROTO=TCP', 'DST=192.168.1.1']
    regex = ''
    temp = []
    
    if len(matchlist) == 1:
        regex = matchlist[0]
    else:
        for _x in range(len(matchlist)):
            match = re.findall('(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', matchlist[_x])
            if match:
                for char in matchlist[_x]:
                    if char is '.':
                        #print 'char = ' + str(char)
                        char = char.replace('.','[.]')
                        temp.append(char)
                    else:
                        temp.append(char)
                
                char = ''.join(temp)
                matchlist [_x] = char
                print matchlist [_x]
            regex = regex +"(?=.*"+ str(matchlist[_x]) +')'
    
    print regex    

            




build_regex()
    