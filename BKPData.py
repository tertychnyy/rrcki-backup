from BKPLogger import BKPLogger
import BKPSite

class BKPData:
    def __init__(self, path):
        #logger
        _logger = BKPLogger().getLogger('BKPData')

        self.name = 'default'
        self.server = 'localhost'
        self.path = '/'
        self.type = 'file'

        site = BKPSite.getJSON(path)

        if site['name'] != None:
            self.name = site['name']
        else:
            self._logger.error("Empty data.name")
        if site['server'] != None:
            self.server = site['server']
        else:
            self._logger.error("Empty data.server")
        if site['path'] != None:
            self.path = site['path']
        else:
            self._logger.error("Empty data.path")
        if site['type'] != None:
            self.type = site['type']
        else:
            self._logger.error("Empty data.type")

    def __str__(self):
        return '[' + self.name + '] ' + self.server + ':' + self.path + ' TYPE:' + self.type