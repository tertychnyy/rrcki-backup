import os
import commands
from BKPLogger import BKPLogger
from BKPSite import BKPSite
from BKPConfig import BKPConfig
from BKPData import BKPData


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
        _logger.debug(loout)

    for site in sites:
        dfs = []
        for root, dirs, files in os.walk(os.path.join(dataconfdir, site.name)):
            for file in files:
                if file.endswith(".json"):
                    df = BKPData(os.path.join(root, file))
                    dfs.append(df)

    for df in dfs:
        if df.type == 'file':
            dirflag = ''
        elif df.type == 'dir':
            dirflag = '/*'
        else:
            _logger.error('Invalid data type: ' + str(df))

        for site in sites:
            if site.name == df.server:
                dfsite = site

        if dfsite != None:
            fromPath = df.path
            toPath = os.path.join(datahome, df.server)
            _cmd = "rsync -avzhe '%s' %s@%s:%s%s %s/" % (dfsite.getSSHHead(), dfsite.user, dfsite.server, fromPath, dirflag, toPath)

            _logger.debug("Trying to rsync data from %s: %s" % (df.server, _cmd))
            lostat, loout = commands.getstatusoutput(_cmd)
            _logger.debug(loout)
        else:
            _logger.error('Datasite not found: ' + str(df))
    exit()


homepath = BKPConfig().getHome()
confdir = os.path.join(homepath, "conf")
sitesdir = os.path.join(confdir, "sites")
dataconfdir = os.path.join(confdir, "data")
serverdataconfdir = BKPConfig().getServerHome()
datahome = BKPConfig().getDataHome()

_logger = BKPLogger().getLogger('backup')

main()