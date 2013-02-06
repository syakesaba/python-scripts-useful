#!/usr/bin/env python
# encoding: utf-8

# put this as ~/.pythonrc
# and
# PYTHONSTARTUP=~/.pythonrc
try:
    import rlcompleter,atexit,os
    pyhistfile=os.getenv("HOME")+"/.pyhistory"
    if not os.path.exists(pyhistfile):
        open(pyhistfile,"w").close()
        os.chmod(pyhistfile,755)
    rlcompleter.readline.parse_and_bind("tab: complete")
    rlcompleter.readline.read_history_file(pyhistfile)
    rlcompleter.readline.set_history_length(100)
    atexit.register(rlcompleter.readline.write_history_file, pyhistfile)
    print "TAB: Complete;Saving History in '%s' " % pyhistfile
    del atexit,rlcompleter,os,pyhistfile
except:
    pass
