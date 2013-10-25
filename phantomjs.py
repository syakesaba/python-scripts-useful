#!/usr/bin/env python
# encdoing: utf-8

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from time import clock

REMOTE_SERVER_IP="x.x.x.x"

REMOTE_SERVER = "http://%s:4444/wd/hub" % REMOTE_SERVER_IP

print "Starting PHANTOMJS Broser..."
driver = webdriver.Remote(
            command_executor=REMOTE_SERVER,
            desired_capabilities=DesiredCapabilities.PHANTOMJS
         )
print "Web Browser is now ready."

try:
    import rlcompleter,atexit,os,code
    pyhistfile=os.getenv("HOME")+"/.pyhistory"
    rlcompleter.readline.parse_and_bind("tab: complete")
    rlcompleter.readline.read_history_file(pyhistfile)
    rlcompleter.readline.set_history_length(1000)
    atexit.register(rlcompleter.readline.write_history_file, pyhistfile)
    atexit.register(driver.quit)
    del os,pyhistfile
except:
    pass

code.interact(banner="driver ENABLED!",local=locals())

