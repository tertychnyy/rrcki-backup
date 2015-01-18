import os
from configobj import ConfigObj

class BKPConfig:
    def __init__(self):
        self.config = ConfigObj('/home/ivan/PyCharm/rrcki-backup/conf/conf.ini')

    def getLogDir(self):
        return os.path.join(self.config.homedir, self.config.logdir)


