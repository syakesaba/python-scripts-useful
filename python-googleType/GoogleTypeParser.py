#!/usr/bin/env python
# encoding: utf-8
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

if __name__ == "__main__":
    my=GoogleTypeParser("<body><img data-letter='A' src='/path/to/dir/dummy.img' /></body>")
    print my.imgSrcList
    print my.imgNameDict
