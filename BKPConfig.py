import os
from configobj import ConfigObj

class BKPConfig:
    def __init__(self):
        self.config = ConfigObj('conf/conf.ini')

    def getLogDir(self):
        return os.path.join(self.config['homedir'], self.config['logdir'])


