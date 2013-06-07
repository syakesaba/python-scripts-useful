#!/usr/bin/env python
# -*- coding: utf-8 -*-

import httplib2
from time import strftime
from bs4 import BeautifulSoup as BS
import re,sys,os
import base64
#import sqlite

class Hissi(object):
    """
    俺よりIDに～～～ｗｗｗｗ
    ってやつを黙らせるためのスクリプト。
    同時にhissi.orgに多大な負荷をかける。
    """
    def __init__(self,board="news4vip"):
        """
        """
        self.DEBUG=True
        self.charset="cp932"#shift-jis
        self.board=board
        self.today=strftime("%Y%m%d")
        self.URI="http://hissi.org/read.php/%s/%s/" % (self.board,self.today)
        self.IDi=self._getHowManyIDs()
        self.maxpage= int( self.IDi / 50)
    def d(self,s):
        if self.DEBUG:
            sys.stderr.write("[*]"+s+os.linesep)

    def _getHowManyIDs(self):
        h,d=httplib2.Http().request(self.URI,"GET")
        if h["status"] == "404":
            raise Exception("日付の変わり目")
        d=d.decode(self.charset)
        return int(BS(d).find("tr").find("tr").find("td").next.next.text)

    def _getIDs(self,URI,start,end):#self.URI
        ids=[]
        h,d=httplib2.Http().request(URI,"GET")
        d=d.decode(self.charset)
        for id in BS(d).findAll("a")[start:end]:
            ids.append(id.text)
        return ids

    def getIDList(self,HowManyIDsYouNeed):
        print HowManyIDsYouNeed 
        ids=list(self._getIDs(self.URI,4,-1))
        self.d("1ページ目読み込み完了...")
        if HowManyIDsYouNeed < 50:
            self.ids=ids
            return
        for i in range(self.maxpage):
            if HowManyIDsYouNeed < (i+2) * 50:
                break
            ids = ids + list(self._getIDs(self.URI + "?p=%s" % str(i+1),5,-2))
            self.d(str(i+2)+"ページ目読み込み完了...")
        self.ids=ids

    def whatIDExist(self,regexp):
        match=[]
        try:reg=re.compile(regexp)
        except:return []
        for ID in self.ids:
            if reg.findall(ID):
                match.append(ID)
        return match

    def pickURLone(self,ID):
        URL=self.URI + base64.encodebytes(ID.encode()).decode()[:-1] + ".html"
        h,d=httplib2.Http(".httplib2").request(URL,"GET")
        a=BS(d.decode("cp932")).findAll("a")
        r=a[4]
        if "すべて表示する" in r.text:
            r=a[5]
        return r.attrs["href"],r.text

if __name__ == "__main__":
    try:
        import rlcompleter
        rlcompleter.readline.parse_and_bind("tab:complete")
    except:
        pass
    my=Hissi()
    my.d(my.today+"/"+my.board)
    my.d("IDは全体で" + str(my.IDi) + "個あります")
    num=int(raw_input("何人分のIDを抽出する？："))
    
    my.getIDList(num)
    while 1:
        reg=raw_input("どんなIDを探す？(正規表現):")
        for ID in my.whatIDExist(reg):
            my.d("hit! =>" + ID)
            #print(my.pickURLone(ID)[0][:-3] + "\n(" + my.pickURLone(ID)[1] + ")")
