import os
from configobj import ConfigObj

class BKPConfig:
    def __init__(self):
        self.config = ConfigObj('/srv/bkp/conf/backup.conf')

    def getLogDir(self):
        return os.path.join(self.getHome(), self.config['logdir'])

    def getHome(self):
        return self.config['homedir']

    def getServerHome(self):
        return self.config['serverhome']

    def getDataHome(self):
        return self.config['datahome']


