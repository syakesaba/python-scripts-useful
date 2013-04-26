#!/usr/bin/env python
# encoding: utf-8¬

from scapy import all
from scapy.utils import *
from scapy.utils import PcapReader
from scapy.layers.inet import *
from scapy.sendrecv import *

import pygame
import time

pygame.init()
pygame.mixer.init()

class MyMusic:
    """
クラス作る必要ない
    """
    def __init__(self):
        self.laser=[]
        for i in range(8):
            self.laser.append(pygame.mixer.Sound("laser/laser0"+str(i+1)+".mp3.wav"))

    def sound(self,pkt):
        arr=self.ipv4RGB(pkt[IP].dst)
        num=arr[0]%8
        self.laser[num].play()

        def ipv4RGB(self,ipv4addr):
                "「.」で分割する。(xxx,xxx,xxx,xxx)のカタチにする。"
                return [int(i) for i in ipv4addr.split(".")]
if __name__=="__main__":
    m=MyMusic()
    sniff(offline="a.cap",lfilter=lambda pkt: IP in pkt,prn=m.sound)
    #sniff(iface='gprs0',lfilter=lambda pkt: IP in pkt,prn=m.sound)
