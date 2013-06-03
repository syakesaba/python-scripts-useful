#!/usr/bin/env python
# encoding: utf-8

import re
import os
import sys
import datetime

import httplib2

DEBUG = True
url = "http://standards.ieee.org/develop/regauth/oui/oui.txt"

dbg = lambda s:sys.stdout.write(str(s) + os.linesep) if DEBUG else None

class FileDownloader:

    def __init__(self, url,filename=""):
        self.url = url
        if filename:
            self.filename = filename
        else:
            self.filename = guessFileNameOfUrl(url)
        self.http = httplib2.Http()
        self.FILENAMES_FOR_GUESS = ["index." + extension for extension in \
                ("html", "htm", "php", "jsp", "cgi" "aspx")]
        self.modDateFile = self.modificationDateOfFile(filename)
        self.modDateUrl = self.modificationDateOfUrl(url)

    def _modificationDateOfFile(self):
        "http://stackoverflow.com/questions/237079/how-to-get-file-creation-modification-date-times-in-python"
        t = os.path.getmtime(self.filename)
        return datetime.datetime.fromtimestamp(t)

    def _modificationDateOfUrl(self):
        "http://forum.hostucan.com/showthread.php?8-Python-parse-http-header-last-modified-to-DateTime"
        header, body = self.http.request(self.url, "HEAD")
        if header["status"] != "200":
            raise HttpStatusNot200Exception(header["status"])
        try:
            lastModified = header[0]["last-modified"]
        except KeyError:
            raise HttpHeaderHasNotLastModifiedTagException(url)
        return datetime.strptime(lastModified, "%a, %d %b %Y %H:%M:%S %Z")

    def _splitFileName(self):
        path_to_file = httplib2.urllib.urlparse(self.url).path
        if path_to_file.endswith("/") or path_to_file == "":
            raise UrlHasNotFileNameException(self.url)
        return data.path.split("/")[-1]

    def update(self, url=url):
        dbg("Headering %s now..." % url)
        header, body = self.http.request(url, "GET")
        if header["status"] != "200":
            raise HttpStatusNot200Exception(header)

    def guessFileNameOfurl(self):
        fileName = ""
        try:
            fileName = self._splitFileName()
        except UrlHasNotFileNameException:
            parsedUrl = httplib2.urlparse.urlparse(self.url)
            if not parsedUrl.path.endswith("/") :
                url = parsedUrl
                url.path += "/"#できない・・・？
                #url = httplib2.urlparse.urlunparse(url)
            for filename in self.FILENAMES_FOR_GUESS:
                #httplib2.urlparse.urlunparse(url.pathfilename)
                #なぜイミュータブルなんだあああああああああああああああああああ
        header, body = self.http.request(self.url,"HEAD")


class HttpStatusNot200Exception(Exception):
    def __init__(self, status):
        self.status = status
    def __str__(self):
        return "HTTP status NOT OK! ==> %s" % str(status)

class HttpHeaderHasNotLastModifiedTagException(Exception):
    def __init__(self, url):
        self.url = url
    def __str__(self):
        return "NO Last-Modified tag in HTTP header of %s" % str(self.url)

class UrlHasNotFileNameException(Exception)
    def __init__(self, url):
        self.url = url
    def __str__(self):
        return "NO FileName seen at %s" % str(self.url)

