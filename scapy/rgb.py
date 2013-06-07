#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scapy.all import *
from scapy.utils import *
import os

import pygame
import pygame.gfxdraw
import pygame.color
#import random # random.radint(0,255)がRGBのテストに使える

class MyGui:
        """
        はっきりいってくらすにするひつようがない
        """
    def __init__(self,gamen_x,gamen_y):
                """
                スクリーンを初期化し、最初の画面を表示する。座標を最初の場所に動かす。
                """
        self.screen=pygame.display.set_mode( (gamen_x,gamen_y)) 
        self.xMax,self.yMax=self.screen.get_size()
        self.x=0
        self.y=0

    def drawDot(self,rbgc):
                """
                (x,y)の位置のドットに色をつける。その後、座標を進める。
                """
        pygame.gfxdraw.pixel(self.screen,self.x,self.y,rbgc)
        #pygame.display.update()
                #self.walkDot()

    def walkDot(self):
        """
        1ドット分、左から右に、x座標を移動させる。
        行末まで言ったらy座標を下移動させ、次の行の左端に移る。
        最後の行の行末までいったらスクリプトを止める。
        """
        if self.x < self.xMax:
            self.x = self.x + 1
        else:
            if self.y < self.yMax:
                self.y = self.y + 1
                                self.x=0
                        else:
                                exit()

        def ipv4RGB(self,ipv4addr):
                "「.」で分割する。(xxx,xxx,xxx,xxx)のカタチにする。"
                return [int(i) for i in ipv4addr.split(".")]

        def ipv6RGB(self,ipv6addr):
                "未。16進数だし、「:」で分割してハッシュみたいに0xFFで割ればなんとかなりそうだが"
                pass

if __name__ == "__main__":
    pygame.init()
    mg=MyGui(800,480)
        def a(p):
                if p.haslayer(IP):
                        rgb= mg.ipv4RGB(p[IP].src)
                        mg.drawDot( rgb )
            mg.walkDot()
                        rgb= mg.ipv4RGB(p[IP].dst)
                        mg.drawDot( rgb )
            mg.walkDot()
            if not (mg.x % 100):
                  pygame.display.update()
                else:
                        print "No IP " 
        sniff(offline="a.cap",prn=a)
        #sniff(iface="wlan0",prn=a)
