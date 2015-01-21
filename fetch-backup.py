#!/usr/bin/env python

import commands, os, sys

RESTORED_DATA_DIR = "/data3/bkp/restore"

def usage():
        print "Tool for retrieving closest git commit before/after given date."
        print "Usage:"
        print "python fetch_backup.py GIT_REPO_PATH before DATE"
        print "python fetch_backup.py GIT_REPO_PATH after DATE"

if __name__ == "__main__":
        if len(sys.argv) != 4:
                usage()
                sys.exit(0)
        git_dir = sys.argv[1]
        beforeafter = sys.argv[2]
        if beforeafter not in ["before", "after"]:
                usage()
                sys.exit(0)
        date = sys.argv[3]


        os.chdir(git_dir)

        #SOMETHING LIKE THIS SHOULD BE USED IF PYTHON >=2.7:
        #output = subprocess.check_output(["git", "log", "--pretty='%h %cd'", "--after={%s}"%(AFTER), "--before={%s}"%(BEFORE)])

        status, output = commands.getstatusoutput("git log --pretty='%%h' --%s={'%s'}"%(beforeafter, date))
        if status != 0:
                print "ERROR: git log: status is %d" % (status)
                print output
                sys.exit(1)
        commits = output.split("\n")
        if beforeafter == "before":
                commithash = commits[0]
        else:
                commithash = commits[len(commits)-1]
        status, output = commands.getstatusoutput("git checkout " + commithash)
        # TO DO: if GIT_REPO_PATH is not a git directory, both checkouts here will fail. Maybe it'll not be much a problem, but this could be done in a more neat way.
        if status != 0:
                print "ERROR: git checkout to commit by hash: status is %d" % (status)
                print output
                print "Trying to revert back to the master branch: 'git checkout master'."
                status, output = commands.getstatusoutput("git checkout master") # This should be taken in account if your git directory was other than master.
                sys.exit(1)

        status, output = commands.getstatusoutput("mkdir -p %s | cp -r ./* %s" % (RESTORED_DATA_DIR, RESTORED_DATA_DIR))
        if status != 0:
                print "ERROR: creating restored data directory and copying files into it: status is %d" % (status)
                print output
                print "Trying to revert back to the master branch: 'git checkout master'."
                status, output = commands.getstatusoutput("git checkout master") # This should be taken in account if your git directory was other than master.
                sys.exit(1)

        status, output = commands.getstatusoutput("git checkout master") # This should be taken in account if your git directory was other than master.
        if status != 0:
                print "ERROR: git checkout ot master: status is %d" % (status)
                print output
                sys.exit(1)
        sys.exit(0)