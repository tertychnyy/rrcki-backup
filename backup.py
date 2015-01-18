import json
import os

import

def getJSON(filepath):
    json_data = open(filepath)
    data = json.load(json_data)
    json_data.close()
    return data

def getSSHParam(site):
    port = ""
    key = ""
    if site['port'] != None:
        port = " -p " + str(site['port'])
    if site['key'] != None:
        key = " -i " + site['key']
    else:
        _logger.error("Site key is not defined")

    return "ssh " + key + port

def main():
    sites = []
    for root, dirs, files in os.walk(sitesdir):
        for file in files:
            if file.endswith(".json"):
                site = getJSON(os.path.join(root, file))
                sites.append(site)
    _logger.debug("Number of sites JSON files: %d", len(sites))

    for site in sites:
        siteObj = BKPSite(site)

        fromPath = serverdataconfdir
        toPath = os.path.join(dataconfdir, siteObj.name)
        _cmd = "rsync -avzhe %s:%s %s" % (siteObj.getSSH(), fromPath, toPath)

        _logger.debug("Trying to rsync: %s" % (_cmd))
        #commands.getstatusoutput('python -c "%s"' % (_cmd))


homepath = "/home/ivan/PyCharm/rrcki-backup"
confdir = os.path.join(homepath, "conf")
sitesdir = os.path.join(confdir, "sites")
dataconfdir = os.path.join(confdir, "data")
serverdataconfdir = "/opt/bkp/data"

_logger = BKPLogger().getLogger('backup.py')

main()