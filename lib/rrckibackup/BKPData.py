from BKPLogger import BKPLogger
import BKPSite

class BKPData:
    def __init__(self, path):
        #logger
        _logger = BKPLogger().getLogger('BKPData')

        self.server = 'localhost'
        self.branchs = []
        self.site = None

        site = BKPSite.getJSON(path)

        self.server = site.keys()[0]
        self.branches = site[self.server].keys()
        self.site = site


    def __str__(self):
        return '[' + self.server + '] '