import json
import os
from BKPLogger import BKPLogger
from BKPSite import BKPSite

def main():
    sites = []
    for root, dirs, files in os.walk(sitesdir):
        for file in files:
            if file.endswith(".json"):
                site = BKPSite(os.path.join(root, file))
                sites.append(site)
    _logger.debug("Number of sites JSON files: %d", len(sites))

    for site in sites:
        fromPath = serverdataconfdir
        toPath = os.path.join(dataconfdir, site.name)
        _cmd = "rsync -avzhe %s:%s %s" % (site.getSSH(), fromPath, toPath)

        _logger.debug("Trying to rsync: %s" % (_cmd))
        #commands.getstatusoutput('python -c "%s"' % (_cmd))

    exit()

homepath = "/home/ivan/PyCharm/rrcki-backup"
confdir = os.path.join(homepath, "conf")
sitesdir = os.path.join(confdir, "sites")
dataconfdir = os.path.join(confdir, "data")
serverdataconfdir = "/opt/bkp/data"

_logger = BKPLogger().getLogger('backup')

main()