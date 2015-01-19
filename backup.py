import os
import commands
import sys
sys.path.append('lib/rrckibackup')
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
        #_logger.debug(loout)

    for site in sites:
        dfs = []
        for root, dirs, files in os.walk(os.path.join(dataconfdir, site.name)):
            for file in files:
                if file.endswith(".json"):
                    df = BKPData(os.path.join(root, file))
                    dfs.append(df)

    for df in dfs:
        homepath = os.path.join(datahome, df.server, df.branch)

        if df.type == 'file':
            dirflag = ''
            toPath = homepath + df.path
        elif df.type == 'dir':
            dirflag = '/'
            toPath = homepath + os.path.join(df.path, df.name)
        else:
            _logger.error('Invalid data type: ' + str(df))

        for site in sites:
            if site.name == df.server:
                dfsite = site

        if dfsite != None:
            fromPath = os.path.join(df.path, df.name)

            _cmd = "mkdir -p %s | " % (toPath)
            _cmd =_cmd + "rsync -avzhe '%s' %s@%s:%s%s %s/" % (dfsite.getSSHHead(), dfsite.user, dfsite.server, fromPath, dirflag, toPath)

            _logger.debug("Trying to rsync data from %s: %s" % (df.server, _cmd))
            lostat, loout = commands.getstatusoutput(_cmd)
            #_logger.debug(loout)
        else:
            _logger.error('Datasite not found: ' + str(df))

    dirs = os.listdir(datahome)
    for dir in dirs:
        ds = os.listdir(os.path.join(datahome, dir))
        for d in ds:
            _cmd = "cd %s ; if [ ! -d .git ] ; then git init ; fi ; git add -A ; git commit -m 'Autocommit'" % (os.path.join(datahome, dir, d))
            _logger.debug("Trying to commit: %s" % (_cmd))
            lostat, loout = commands.getstatusoutput(_cmd)
            #_logger.debug(loout)



homepath = BKPConfig().getHome()
confdir = os.path.join(homepath, "conf")
sitesdir = os.path.join(confdir, "sites")
dataconfdir = os.path.join(confdir, "data")
serverdataconfdir = BKPConfig().getServerHome()
datahome = BKPConfig().getDataHome()

_logger = BKPLogger().getLogger('backup')

main()