import os
import commands
import sys
sys.path.append('lib/rrckibackup')
from BKPLogger import BKPLogger
from BKPSite import BKPSite
from BKPConfig import BKPConfig
from BKPData import BKPData
from BKPUnit import BKPUnit


def main(freq):
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

    dfs = []
    for site in sites:
        for root, dirs, files in os.walk(os.path.join(dataconfdir, site.name)):
            for file in files:
                if file.endswith(".json"):
                    df = BKPData(os.path.join(root, file))
                    for branch in df.branches:
                        # append dirs of branch
                        ddd = df.site[df.server][branch][freq]['dir']
                        for dddd in ddd:
                            dfs.append(BKPUnit(df.server, branch, dddd, 'dir'))
                        # append files of branch
                        fff = df.site[df.server][branch][freq]['file']
                        for ffff in fff:
                            dfs.append(BKPUnit(df.server, branch, ffff, 'file'))

    for df in dfs:
        print df.path
        homepath = os.path.join(datahome, df.server, df.branch)

        if df.type == 'file':
            dirflag = ''
            toPath = homepath + df.path[:-len(df.path.rsplit('/', 1)[1])]
        elif df.type == 'dir':
            dirflag = '/'
            toPath = homepath + df.path
        else:
            _logger.error('Invalid data type: ' + str(df))

        for site in sites:
            if site.name == df.server:
                dfsite = site

        if dfsite is not None:
            fromPath = df.path

            _cmd = "mkdir -p %s | " % (toPath)
            _cmd =_cmd + "rsync -avzhe '%s' %s@%s:%s%s %s%s" % (dfsite.getSSHHead(), dfsite.user, dfsite.server, fromPath, dirflag, toPath, dirflag)

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

main(sys.argv[1])