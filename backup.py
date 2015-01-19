import os
import commands
from BKPLogger import BKPLogger
from BKPSite import BKPSite
from BKPConfig import BKPConfig

def main():
    print sitesdir
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
        _cmd = "rsync -avzhe '%s' %s@%s:%s/* %s/" % (site.getSSHHead(), site.user, site.server, fromPath, toPath)

        _logger.debug("Trying to rsync: %s" % (_cmd))
        lostat, loout = commands.getstatusoutput(_cmd)
        print loout
    exit()

homepath = BKPConfig().getHome()
confdir = os.path.join(homepath, "conf")
sitesdir = os.path.join(confdir, "sites")
dataconfdir = os.path.join(confdir, "data")
serverdataconfdir = BKPConfig().getServerHome()

_logger = BKPLogger().getLogger('backup')

main()