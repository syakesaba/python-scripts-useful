#!/usr/bin/env python
# encoding: utf-8

#BOLD
def bblack(s):
    return "\x1B[1m\x1B[30m" + s + "\x1B[0m"
def bred(s):
    return "\x1B[1m\x1B[31m" + s + "\x1B[0m"
def bgreen(s):
    return "\x1B[1m\x1B[32m" + s + "\x1B[0m"
def byellow(s):
    return "\x1B[1m\x1B[33m" + s + "\x1B[0m"
def bblue(s):
    return "\x1B[1m\x1B[34m" + s + "\x1B[0m"
def bmagenta(s):
    return "\x1B[1m\x1B[35m" + s + "\x1B[0m"
def bcyan(s):
    return "\x1B[1m\x1B[36m" + s + "\x1B[0m"
def bwhite(s):
    return "\x1B[1m\x1B[37m" + s + "\x1B[0m"

#BRIGHT
def lblack(s):
    return "\x1B[0m\x1B[30m" + s + "\x1B[0m"
def lred(s):
    return "\x1B[0m\x1B[31m" + s + "\x1B[0m"
def lgreen(s):
    return "\x1B[0m\x1B[32m" + s + "\x1B[0m"
def lyellow(s):
    return "\x1B[0m\x1B[33m" + s + "\x1B[0m"
def lblue(s):
    return "\x1B[0m\x1B[34m" + s + "\x1B[0m"
def lmagenta(s):
    return "\x1B[0m\x1B[35m" + s + "\x1B[0m"
def lcyan(s):
    return "\x1B[0m\x1B[36m" + s + "\x1B[0m"
def lwhite(s):
    return "\x1B[0m\x1B[37m" + s + "\x1B[0m"

#NORMAL
def black(s):
    return "\x1B[2m\x1B[30m" + s + "\x1B[0m"
def red(s):
    return "\x1B[2m\x1B[31m" + s + "\x1B[0m"
def green(s):
    return "\x1B[2m\x1B[32m" + s + "\x1B[0m"
def yellow(s):
    return "\x1B[2m\x1B[33m" + s + "\x1B[0m"
def blue(s):
    return "\x1B[2m\x1B[34m" + s + "\x1B[0m"
def magenta(s):
    return "\x1B[2m\x1B[35m" + s + "\x1B[0m"
def cyan(s):
    return "\x1B[2m\x1B[36m" + s + "\x1B[0m"
def white(s):
    return "\x1B[2m\x1B[37m" + s + "\x1B[0m"

#BGBOLD
def bgbblack(s):
    return "\x1B[1m\x1B[40m" + s + "\x1B[0m"
def bgbred(s):
    return "\x1B[1m\x1B[41m" + s + "\x1B[0m"
def bgbgreen(s):
    return "\x1B[1m\x1B[42m" + s + "\x1B[0m"
def bgbyellow(s):
    return "\x1B[1m\x1B[43m" + s + "\x1B[0m"
def bgbblue(s):
    return "\x1B[1m\x1B[44m" + s + "\x1B[0m"
def bgbmagenta(s):
    return "\x1B[1m\x1B[45m" + s + "\x1B[0m"
def bgbcyan(s):
    return "\x1B[1m\x1B[46m" + s + "\x1B[0m"
def bgbwhite(s):
    return "\x1B[1m\x1B[47m" + s + "\x1B[0m"

#BGBRIGHT
def bglblack(s):
    return "\x1B[0m\x1B[40m" + s + "\x1B[0m"
def bglred(s):
    return "\x1B[0m\x1B[41m" + s + "\x1B[0m"
def bglgreen(s):
    return "\x1B[0m\x1B[42m" + s + "\x1B[0m"
def bglyellow(s):
    return "\x1B[0m\x1B[43m" + s + "\x1B[0m"
def bglblue(s):
    return "\x1B[0m\x1B[44m" + s + "\x1B[0m"
def bglmagenta(s):
    return "\x1B[0m\x1B[45m" + s + "\x1B[0m"
def bglcyan(s):
    return "\x1B[0m\x1B[46m" + s + "\x1B[0m"
def bglwhite(s):
    return "\x1B[0m\x1B[47m" + s + "\x1B[0m"

#BGNORMAL
def bgblack(s):
    return "\x1B[2m\x1B[40m" + s + "\x1B[0m"
def bgred(s):
    return "\x1B[2m\x1B[41m" + s + "\x1B[0m"
def bggreen(s):
    return "\x1B[2m\x1B[42m" + s + "\x1B[0m"
def bgyellow(s):
    return "\x1B[2m\x1B[43m" + s + "\x1B[0m"
def bgblue(s):
    return "\x1B[2m\x1B[44m" + s + "\x1B[0m"
def bgmagenta(s):
    return "\x1B[2m\x1B[45m" + s + "\x1B[0m"
def bgcyan(s):
    return "\x1B[2m\x1B[46m" + s + "\x1B[0m"
def bgwhite(s):
    return "\x1B[2m\x1B[47m" + s + "\x1B[0m"

colors = ["black", "red","green","yellow","blue","magenta","cyan","white"]
lcolors = ["l" + color for color in colors]
bcolors = ["b" + color for color in colors]

bgcolors = ["bg" + color for color in colors]
bglcolors = ["bgl" + color for color in colors]
bgbcolors = ["bgb" + color for color in colors]

colors += lcolors
colors += bcolors
colors += bgcolors
colors += bglcolors
colors += bgbcolors

if __name__ == "__main__":
    import sys
    for color in colors:
        eval("sys.stdout.write(%s('%s') + '\\r\\n')" % (color,color) )
