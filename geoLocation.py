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

    一切エラー処理をしていません。
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
        """
        bssid: BSSID
        essid: ESSID (optional)
        rssi: RSSI (semi-must){Specifying real RSSI value will increase the certainty}
        """
        self._isValidBSSID(bssid)
        self.towers.append({"mac":str(bssid),"ssid":str(essid),"ss":str(rssi)})

    def removeAP(self,bssid):
        """
        bssid: BSSID
        """
        for ap in self.towers:
            if ap["mac"] == bssid:
                self.towers.remove(ap)

    def send(self):
        """
        -> json
        """
        req=self.apiURL + \
        self._parameterize() + \
        "&browser=%s&sensor=%s" % (self.browser, self.sensor)
        response=urllib2.urlopen(req)
        ret_json=response.read()
        ret=self._decoder.decode(ret_json)
        return ret

    def _isValidBSSID(self,bssid):
        """
        bssid: BSSID
        """
        if self._re_bssid.match(bssid) == None:
            #raise Exception("Invalid BSSID %s." % bssid)
            return False
        return True

    def _isValidAccuracy(self,accuracy):
        """
        Check Google sent pre-defined value of BAD_ACCURACY or didnt
        accuracy: The received, from Google's geolocationAPI
        """
        if accuracy in self.ACCURACY_BADTOWER:
            return False
        return True

    def _isEnoughAPs(self):
        """
        the Google reject people identify someone with ease
        """
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
        """
        rssi=RSSI
        maxrssi=the Highest RSSI value seen in a while

        -> int
        """
        return int((rssi*1.0/maxrssi*1.0+0.00000001)*100)

    def w2dbm(self,mW):
        """
        mW: Milli Watt, 1W = 1000mW.

        -> dBm
        """
        return 10.0*log10(w)

    def percentage2dbm(self,p):
        """
        Vendor?IEEE802.11?
        """
        #return fromVendorDB(p)
        pass

#############
if __name__ == "__main__":
    my=GoogleGeoLocationAPI()
    test1="00:18:84:20:E6:3B"
    test2="00:18:84:20:E6:39"
    my.addAP(bssid=test1,essid="",rssi=-70)
    my.addAP(bssid=test2,essid="",rssi=-70)
    print "TEST1 : " + test1
    print "TEST2 : " + test2
    ret = my.send()
    if ret["status"] != "OK":
        print "[*]Status is not OK."
        print ret
    accuracy=ret["accuracy"]
    if accuracy in my.ACCURACY_BADTOWER:
        print "[*] BAD TOWER! Google will provide the location using your IP!"
        print ret
    print "[*] Accuracy: %s" % accuracy
    lat=str(ret["location"]["lat"])
    lng=str(ret["location"]["lng"])
    print "[*] See also:"
    t="http://maps.googleapis.com/maps/api/geocode/json?latlng=%s,%s&sensor=true"\
    % (lat,lng)
    print t
    print "https://maps.google.com/maps?q=%s,%s&iwloc=A&hl=ja" \
    % (lat,lng)
    rret=my._decoder.decode(urllib2.urlopen(t).read())
    print "____result____"
    print rret["results"][0]["formatted_address"]
