#/usr/bin/env python
# encoding: utf-8

from urllib import urlencode
from httplib2 import Http
from os import linesep

from GoogleTypeParser import GoogleTypeParser

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
