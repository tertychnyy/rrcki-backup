import json

from BKPLogger import BKPLogger

def getJSON(filepath):
        json_data = open(filepath)
        data = json.load(json_data)
        json_data.close()
        return data

class BKPSite:
    def __init__(self, path):
        #logger
        _logger = BKPLogger().getLogger('BKPSite')

        self.name = 'default'
        self.server = '127.0.0.1'
        self.user = 'root'
        self.port = 22
        self.key = ''

        site = getJSON(path)

        if site['name'] != None:
            self.name = site['name']
        else:
            self._logger.error("Empty site.name")
        if site['server'] != None:
            self.server = site['server']
        else:
            self._logger.error("Empty site.server")
        if site['user'] != None:
            self.user = site['user']
        else:
            self._logger.error("Empty site.server")
        if site['port'] != None:
            self.port = site['port']
        else:
            self._logger.error("Empty site.port")
        if site['key'] != None:
            self.key = site['key']
        else:
            self._logger.error("Empty site.key")

    def getSSH(self):
        ssh = self.getSSHHead() + " " + self.user + "@" + self.server
        return ssh

    def getSSHHead(self):
        ssh = 'ssh -i ' + self.key + " -p " + str(self.port)
        return ssh

