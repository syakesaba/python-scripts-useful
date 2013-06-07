#!/usr/bin/env python
# encoding: utf-8

from scapy.all import *
def ipNukinuki(pkt):
    print pkt[IP].src
    print pkt[IP].dst
def isIP(pkt):
    return IP in pkt
sniff(count=50,offline="a.cap",lfilter=isIP,prn=ipNukinuki)
