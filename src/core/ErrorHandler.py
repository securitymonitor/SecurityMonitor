'''
Created on 11 mrt. 2013

@author: stanley numan
'''
import logging

#logging settings
logger = logging.getLogger('SecurityMonitor')
hdlr = logging.FileHandler('/var/tmp/SecurityMonitor.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr) 
logger.setLevel(logging.WARNING)




if __name__ == '__main__':
    pass
while True:
    try:
        x = int(raw_input("Toets in getal in: "))
        print ("Thanks, je nummer was:"),x
        break
    except ValueError:
        logger.error('Er is geen getal ingetoetst.')
#        logger.info('')
#except zorgt voor de error reporting naar log.
#logger.info kan ook, ligt aan het loglevel.
