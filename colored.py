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
    return "\x1B[0m\x1B[30m;" + s + "\x1B[0m"
def lred(s):
    return "\x1B[0m\x1B[30m" + s + "\x1B[0m"
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
    return "\x1B[2m\x1B[30m;" + s + "\x1B[0m"
def red(s):
    return "\x1B[2m\x1B[32m" + s + "\x1B[0m"
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

colors = ["black","green","yellow","blue","magenta","cyan","white"]
lcolors = ["l" + color for color in colors]
bcolors = ["b" + color for color in colors]

colors += lcolors
colors += bcolors

if __name__ == "__main__":
    import sys
    sys.stdout.write(black("black"))
    sys.stdout.write(green("green"))
    sys.stdout.write(yellow("yellow"))
    sys.stdout.write(blue("blue"))
    sys.stdout.write(magenta("magenta"))
    sys.stdout.write(cyan("cyan"))
    sys.stdout.write(white("white"))

    sys.stdout.write(lblack("lblack"))
    sys.stdout.write(lgreen("lgreen"))
    sys.stdout.write(lyellow("lyellow"))
    sys.stdout.write(lblue("lblue"))
    sys.stdout.write(lmagenta("lmagenta"))
    sys.stdout.write(lcyan("lcyan"))
    sys.stdout.write(lwhite("lwhite"))

    sys.stdout.write(bblack("bblack"))
    sys.stdout.write(bgreen("bgreen"))
    sys.stdout.write(byellow("byellow"))
    sys.stdout.write(bblue("bblue"))
    sys.stdout.write(bmagenta("bmagenta"))
    sys.stdout.write(bcyan("bcyan"))
    sys.stdout.write(bwhite("bwhite"))

    def test(s):
        return "\x1B[6m\x1B[34m" + s + "\x1B[0m"
    sys.stdout.write(test("test"))
    sys.stdout.write("\r\n")
