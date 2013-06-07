#/usr/bin/env python
# encoding: utf-8

__author__ = "syakesaba"

from urllib import urlencode
from httplib2 import Http
from os import linesep
try:
    from html.parser import HTMLParser
except:
    from HTMLParser import HTMLParser

class GoogleTypeParser(HTMLParser):
    """
    """
    def __init__(self,html_source):
        HTMLParser.__init__(self)
        self.imgSrcList = []
        self.imgNameDict = {}
        self.feed(html_source)
    def handle_starttag(self, tag, attrs):
        if tag == "img":
            attrs = dict(attrs)
            if "src" in attrs:
                self.imgSrcList.append(attrs["src"])
            if "data-letter" in attrs:
                if not self.imgNameDict.has_key(attrs["data-letter"]):
                    self.imgNameDict.update({attrs["data-letter"]:[]})
                self.imgNameDict[attrs["data-letter"]].append(attrs["src"])
    def handle_endtag(self, tag):
        pass

    def handle_data(self, data):
        pass

class GoogleType:

    def __init__(self):
        self.h = Http()
        self._URI = "http://www.google-type.com"
        self._API_URI = "%s/genimg.php" % self._URI
        self._HEADERS_MUST = {"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"}

    def get(self, s):
        header, body = self.h.request(uri=self._API_URI, method="POST",
                                    body=urlencode({"q":s}), headers=self._HEADERS_MUST)
        if header["status"] != "200":
            raise Exception("Cant Connect to %s" % self._API_URI)
        return body

    def parse(self, body):
        p = GoogleTypeParser(body)
        #return linesep.join([self._URI+s for s in p.imgSrcList])
        return [self._URI + "/" + s for s in p.imgSrcList]

    def printD(self, body):
        p = GoogleTypeParser(body)
        #return linesep.join([self._URI+s for s in p.imgSrcList])
        for key in p.imgNameDict:
            for s in p.imgNameDict[key]:
                print "%s %s" % (key, self._URI + "/" + s)


if __name__ == "__main__":
    from sys import stdin,stderr,argv
    my = GoogleType()
    if len(argv) > 1:
        t = argv[1]
    else:
        stderr.write("[*]Type Any String: ")
        t = stdin.readline()[:-len(linesep)]
    stderr.write("[*]Wait A while..." + linesep)
    #t.decode("utf-8")
    body = my.get(t)
    print linesep.join(my.parse(body))
    print ""
    my.printD(body)
