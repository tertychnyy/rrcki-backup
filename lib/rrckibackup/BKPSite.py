import json
import sys

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

        if site['name'] is not None:
            self.name = site['name']
        else:
            self._logger.error("Empty site.name")
            sys.exit(1)
        if site['server'] is not None:
            self.server = site['server']
        else:
            self._logger.error("Empty site.server")
            sys.exit(1)
        if site['user'] is not None:
            self.user = site['user']
        else:
            self._logger.error("Empty site.server")
            sys.exit(1)
        if site['port'] is not None:
            self.port = site['port']
        else:
            self._logger.error("Empty site.port")
            sys.exit(1)
        if site['key'] is not None:
            self.key = site['key']
        else:
            self._logger.error("Empty site.key")
            sys.exit(1)

    def getSSH(self):
        ssh = self.getSSHHead() + " " + self.user + "@" + self.server
        return ssh

    def getSSHHead(self):
        ssh = 'ssh -i ' + self.key + " -p " + str(self.port)
        return ssh

