import os
from configobj import ConfigObj

class BKPConfig:
    def __init__(self):
        self.config = ConfigObj('conf/conf.ini')

    def getLogDir(self):
        return self.config['logdir']

    def getHome(self):
        return self.config['homedir']

    def getServerHome(self):
        return self.config['serverhome']


