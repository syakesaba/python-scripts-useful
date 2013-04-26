#!/usr/bin/env python3
# encoding: utf-8

(print) # this is a python3 script. not python2.

import nkf # NKF wrapper for python3. See; http://sourceforge.jp/projects/nkf/scm/git/nkf/tree/master

try: #  BeautifulSoup,The best HTML parser python,is available to python3 after 2to3.
    from bs4 import BeautifulSoup as BSoup
except:
    from BeautifulSoup import BeautifulSoup as BSoup
import urllib.request
from sys import argv

AURI="http://osu.ppy.sh/pages/include/profile-general.php?u=1679287"
if len(argv) <= 1:
    URI=AURI
else:
    URI=argv[1]
bHtml = urllib.request.urlopen(URI).read()
charset = nkf.guess(bHtml)
sHtml = bHtml.decode(charset)
print(BSoup(sHtml).prettify().decode())
