rrcki-backup
============
Backup locally files from your servers.

Use rsync for data sync

Save changes history with git

Configuration
-------------
Sites JSONs local dir: conf/sites (ex: conf/sites/defaultserver.json.EXAMPLE)

Dirs/Files JSONs remote dir: serverhome (default: /srv/bkp/data) (ex: conf/data/defaultserver.json.EXAMPLE)

Storage dir: datahome (default: /storage/bkp)

Usage
-----
    python backup.py daily/weekly/monthly
