import json
import os
import logging
import commands
from configobj import ConfigObj
#azaza

def getJSON(filepath):
    """

    :param filepath:
    :return dataobj:
    """
    json_data = open(filepath)
    data = json.load(json_data)
    json_data.close()
    return data


def getConfig(configpath):
    """

    :param configpath:
    :return configObj:
    """
    config = ConfigObj(configpath)
    return config

def getSSH(site):
    server = site.server
    port = site.port
    user = site.user
    key = site.key

    ssh = str.join("ssh -i ", key, " -p ", str(port), " ", user, "@", server)
    logging.debug(str.join("Prepearing ssh tunnel: ", ssh))
    return ssh

def main():
    sitesconfigpath = '/root/bkp/config/sites'

    logging.basicConfig(filename='backup.log', level=logging.DEBUG)

    sites = []
    for root, dirs, files in os.walk(sitesconfigpath):
        for file in files:
            if file.endswith(".json"):
                site = getJSON(os.path.join(root, file))
                sites.append(site)

    for site in sites:
        fromPath = ""
        toPath = ""
        _cmd = ""

        _cmd = str.join(_cmd, getSSH(site))
        _cmd = str.join(_cmd, " | ")
        _cmd = str.join(_cmd, "rsync -n -av ", fromPath, " ", toPath)


main