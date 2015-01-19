from BKPLogger import BKPLogger
import BKPSite

class BKPUnit:
    def __init__(self, server, branch, path, type):
        #logger
        _logger = BKPLogger().getLogger('BKPUnit')

        self.server = 'localhost'
        self.branch = 'default'
        self.path = '/'
        self.type = 'dir'

        self.server = server
        self.branch = branch
        self.path = path
        self.type = type

    def __str__(self):
        return '[' + self.server + ':' + self.branch + '] ' + self.path + " TYPE: " + self.type