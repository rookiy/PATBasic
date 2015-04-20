#!/usr/bin/env python
import sys
import re

Pattern = re.compile(r'([-0-9]*)/([0-9]*) ([-0-9]*)/([0-9]*)')

def gcd(x, y):
    if x%y == 0:
        return y
    else:
        return gcd(y, x%y)

def abs(x):
    if x >= 0:
        return x
    else:
        return x*-1

def num2str(a, b):
    if a%b == 0 :
        return str(a/b)
    else :
        p = gcd(a, b)
        if abs(a) < b:
            return str(a/p)+'/'+str(b/p)
        else:
            if a > 0:
                return str(a/b)+' '+str(a%b/p)+'/'+str(b/p)
            else:
                return '-'+str(abs(a)/b)+' '+str(abs(a)%b/p)+'/'+str(b/p)

def wrap(s):
    if s.startswith('-'):
        return '(%s)' % s
    else :
        return s

def main():
    sys.stdin = open('./1.txt', 'r')
    match = Pattern.match(raw_input())
    a1, b1, a2, b2 = map(int, match.groups())
    
    x = wrap(num2str(a1, b1))
    y = wrap(num2str(a2, b2))
    
    # +
    ap = a1*b2 + a2*b1
    bp = b1*b2
    ansp = wrap(num2str(ap, bp))
    print '%s + %s = %s' % (x, y, ansp)
    
    # -
    am = a1*b2 - a2*b1
    bm = b1*b2
    ansm = wrap(num2str(am, bm))
    print '%s - %s = %s' % (x, y, ansm)
    
    # *
    amp = a1*a2
    bmp = b1*b2
    ansmp = wrap(num2str(amp, bmp))
    print '%s * %s = %s' % (x, y, ansmp)
    
    # /
    ad = a1*b2
    bd = b1*a2
    if bd == 0 :
        ansd = 'Inf'
    else:
        if bd < 0:
            ad, bd = ad*-1, bd*-1
        ansd = wrap(num2str(ad, bd))
    print '%s / %s = %s' % (x, y, ansd)
    

if __name__ == '__main__':
    main()
