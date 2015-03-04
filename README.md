rrcki-backup
============
Backup scripts for your remote servers.
Based on rsync and git

Configuration
-------------
Master:
*   Add lib/rrckibackup to PYTHONPATH
*   Set 'datahome' in conf/backup.conf (default: /storage/bkp)
*   Set sites JSONs in conf/sites (ex: conf/sites/defaultserver.json.EXAMPLE)
*   Set cron daily/weekly/monthly jobs 
     
Servers:
*   Describe dirs/files to backup in /srv/bkp/data/%servername%.json (ex: conf/data/defaultserver.json.EXAMPLE)

Usage
-----
    python backup.py daily/weekly/monthly
