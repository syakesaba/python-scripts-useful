#!/usr/bin/env python
# encoding: utf-8

class Str(str):
    """
    Super String
    """
    def __init__(self, s=""):
        str(s)

    def __sub__(self, s):
        """
        Str("ABC") - "BC" -> Str("A")
        Str("ABC") - "AC" -> Str("ABC")
        """
        if self.endswith(s):
            return Str(self[:-len(s)])
        else:
            return self

    def __div__(self, s):
        """
        Str("ABC") / "B" -> Str("AC")
        Str("ABC") / "AC" -> Str("ABC")
        """
        return Str( self.replace(s, ""))

    def __mul__(self, i):
        """
        Str("ABC") * 2 -> Str("ABCABC")
        """
        if i < 0:
            raise Exception("Reason: %s is not int() or lower Zero " % i)
        return Str(("".join([self for j in range(i)])))

    #def __pow__(self, i):
    def __lshift__(self, si):
        """
        Str("ABC") << 1 -> Str("BC")
        Str("ABC") << "AB" -> Str("C")
        Str("ABC") << "BA" -> Str("ABC")
        """
        if isinstance(si,basestring):
            if self.startswith(si):
                return Str(self[len(si):])
        else:
            return Str(self[si:])
    def __rshift__(self, si):
        """
        Str("ABC") >> 1 -> Str("AB")
        Str("ABC") >> "BC" -> Str("A")
        Str("ABC") >> "CB" -> Str("ABC")
        """
        if isinstance(si,basestring):
            if self.endswith(si):
                return self - si
        else:
            return Str(self[:-si])
    def __xor__(self, s):
        """
        Str("ABC") ^ "ADC" -> 
        """
        pass
    def __neg__(self):
        """
        -Str("ABC") -> Str("CBA")
        """
        return Str("".join([s for s in reversed(self)]))
    def __pos__(self):
        """
        +Str("1A2C3B") -> Str("123ABC")
        """
        return Str("".join([s for s in sorted(self)]))
    def __abs__(self):
        """
        abs(Str("ABC")) ->
        """
        pass
    def __invert__(self):
        """
        ~Str("ABC") ->
        """
        pass
    def __getitem__(self, si):
        if isinstance(si, basestring):
            return self.find(si)
        return Str(str(self)[si])
    #def __setitem__(self,si,s):
    #def __delitem__(self,i):
    #def __getslice__
    #def __setslice__
    #def __delslice__

if __name__ == "__main__":
    import sys
    import os
    p=lambda s:sys.stderr.write(str(s))
    n=os.linesep
    i=lambda: sys.stdin.readline()[:-len(n)]
    def eva(a1,a2,a3):
        if a1:
            p("Str(%s) %s %s" % (a1,a2,a3))
            p(" -> ")
            p(eval("Str(%s) %s %s" % (a1,a2,a3)))
        else:
            p("%s" % a3)
            p(" -> ")
            p(eval("%s" % a3))
        p(n)
    eva("'ABC'","+","'B'")
    eva("'ABC'","-","'B'")
    eva("'ABC'","/","'B'")
    eva("'ABC'","*","3")
    eva("'ABC'",">>","2")
    eva("'ABC'","<<","1")
    eva("","","-Str('ABCDVXYZ')")
    eva("","","+Str('ABDFSAAFS')")
