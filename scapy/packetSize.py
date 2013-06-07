#!/usr/bin/env python
# encoding: utf-8

from scapy.all import *
import sys

p=sys.stdout.write

def sumAndStat(pkt):
    p(str(len(pkt)) + " ")
sniff(offline="a.cap",prn=sumAndStat)
