import time
from Configuration import Configuration
from Monitor import Monitor

def main():
    config= Configuration()
    monitor = Monitor()

    monitor.Monitor()

    sleeptimer = float(config.sleeptimer)
    time.sleep(sleeptimer)
    
if __name__ == '__main__':
    main()
