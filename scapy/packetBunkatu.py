#!/usr/bin/env python
# encoding: utf-8
from scapy.all import rdpcap,wrpcap
from sys import argv
if len(argv) < 4:
    print argv[0], "<inputCap>", "<N>", "<OutputCap>"
    exit(-1)
wrpcap(argv[3],rdpcap(filename=argv[1],count=int(argv[2])))
