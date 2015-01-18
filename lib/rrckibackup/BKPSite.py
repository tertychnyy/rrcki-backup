from lib.rrckibackup import BKPLogger


class BKPSite:
    def __init__(self, site):
        #logger
        _logger = BKPLogger.getLogger('BKPSite')

        self.name = 'default'
        self.server = '127.0.0.1'
        self.user = 'root'
        self.port = 22
        self.key = ''

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

    def getSSHHead(self):
        sshhead = 'ssh -i ' + self.key + " -p " + self.port
        return sshhead

    def getSSH(self):
        ssh = self.getSSHHead() + " " + self.user + "@" + self.server
        return ssh