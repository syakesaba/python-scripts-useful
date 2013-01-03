#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import sys
import os
import re
import urllib2
from math import log10

API="https://maps.googleapis.com/maps/api/browserlocation/json?"
BSSID=r"([a-f|A-F|0-9]{2}[:-]){5}[a-f|A-F|0-9]{2}"

class GoogleGeoLocationAPI:
    """
    See: http://milo2012.wordpress.com/tag/wifi-location/
    Googleは所持するDBから、無線LANアクセスポイントのBSSIDとRSSIにより
    位置情報を測量します。APは２つだけ(!?)でも大丈夫らしいです。
    """

    def __init__(self, apiURL=API, browser="firefox", sensor="true"):
        """
        apiURL=%s
        browser="firefox","chrome","ie",etc.
        sensor="true","false"
        """ % API
        self.apiURL=apiURL
        self.browser=browser
        self.sensor=sensor
        self.towers = []
        self._decoder = json.JSONDecoder()
        self._re_bssid=re.compile(BSSID)
        self.ACCURACY_BADTOWER=[166000.0,122000.0]

    def addAP(self, bssid, essid="", rssi=80):
        self._isValidBSSID(bssid)
        self.towers.append({"mac":str(bssid),"ssid":str(essid),"ss":str(rssi)})

    def removeAP(self,bssid):
        for ap in self.towers:
            if ap["mac"] == bssid:
                self.towers.remove(ap)

    def send(self):
        """
        エラー処理　無視
        """
        req=self.apiURL + \
        self._parameterize() + \
        "&browser=%s&sensor=%s" % (self.browser, self.sensor)
        response=urllib2.urlopen(req)
        ret_json=response.read()
        ret=self._decoder.decode(ret_json)
        return ret

    def _isValidBSSID(self,bssid):
        if self._re_bssid.match(bssid) == None:
            return False
        return True

    def _isValidAccuracy(self,accuracy):
        if accuracy in self.ACCURACY_BADTOWER:
            return False
        return True

    def _isEnoughAPs(self):
        if len(self.towers) < 2:
            return False
        return True

    def _parameterize(self):
        """
        [{"mac":"test","ssid":"test2"},{...},]

        -> "wifi=mac:test|ssid:test&wifi=mac:test2|ssid:test2|ss:test2"
        """
        if not self._isEnoughAPs():
            raise Exception(" Not enough WiFi AP BSSIDs")
        parameterized=[]
        for t in [ap for ap in self.towers if ap]:
            parameterized.append(
            "wifi=" + "|".join([k + ":" + t[k] for k in t.keys() if t[k] ])
            )
        return "&".join(parameterized)

    def rssi2percentage(self,rssi,maxrssi):
        return int((rssi*1.0/maxrssi*1.0)*100)

    def w2dbm(self,w):
        return math.log10(w/0.001)

    def percentage2dbm(self,p):
        #return fromVendorDB(p)
        pass

#############
if __name__ == "__main__":
    my=GoogleGeoLocationAPI()
    my.addAP(bssid="00:18:84:20:E6:3B",essid="",rssi=-70)
    my.addAP(bssid="00:18:84:20:E6:39",essid="",rssi=-70)
    ret = my.send()
    if ret["status"] != "OK":
        print "[*]Status is not OK."
        print ret
    accuracy=ret["accuracy"]
    lat=str(ret["location"]["lat"])
    lng=str(ret["location"]["lng"])
    if accuracy in my.ACCURACY_BADTOWER:
        print "[*] BAD TOWER! Google will provide location using your IP!"
        print ret
    print "[*]Accuracy: %s" % accuracy
    print "[*] See also:"
    t="http://maps.googleapis.com/maps/api/geocode/json?latlng=%s,%s&sensor=true"\
    % (lat,lng)
    print t
    print "https://maps.google.com/maps?q=%s,%s&iwloc=A&hl=ja" \
    % (lat,lng)
    rret=my._decoder.decode(urllib2.urlopen(t).read())
    print rret["results"][0]["formatted_address"]
