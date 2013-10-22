#!/usr/bin/env python
# encoding: utf-8

#Black Red Green Yellow[11]  Blue Magenta Cyan White
def black(s):
    return "\x1B[1m\x1B[30m" + s + "\x1B[0m"
def red(s):
    return "\x1B[1m\x1B[31m" + s + "\x1B[0m"
def green(s):
    return "\x1B[1m\x1B[32m" + s + "\x1B[0m"
def yellow(s):
    return "\x1B[1m\x1B[33m" + s + "\x1B[0m"
def blue(s):
    return "\x1B[1m\x1B[34m" + s + "\x1B[0m"
def magenta(s):
    return "\x1B[1m\x1B[35m" + s + "\x1B[0m"
def cyan(s):
    return "\x1B[1m\x1B[36m" + s + "\x1B[0m"
def white(s):
    return "\x1B[1m\x1B[37m" + s + "\x1B[0m"
lgray = white

def lblack(s):
    return "\x1B[1m\x1B[30m;" + s + "\x1B[0m"
gray = lblack
def lred(s):
    return "\x1B[1m\x1B[31m" + s + "\x1B[0m"
def lgreen(s):
    return "\x1B[1m\x1B[32m" + s + "\x1B[0m"
def lyellow(s):
    return "\x1B[1m\x1B[33m" + s + "\x1B[0m"
def lblue(s):
    return "\x1B[1m\x1B[34m" + s + "\x1B[0m"
def lmagenta(s):
    return "\x1B[1m\x1B[35m" + s + "\x1B[0m"
pink=lmagenta
def lcyan(s):
    return "\x1B[1m\x1B[36m" + s + "\x1B[0m"
skyblue=lcyan
def lwhite(s):
    return "\x1B[1m\x1B[37m" + s + "\x1B[0m"
white = lwhite

colors = ["black","green","yellow","blue","magenta","cyan","white"]
colors += ["l" + color for color in colors]
