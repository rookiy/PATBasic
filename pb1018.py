#!/usr/bin/env python
import sys
from decorator4 import performance

def most(resX, resY):
    if resX['B']>=resX['C'] and resX['B']>=resX['J']:
        x = 'B'
    elif resX['C']>=resX['J']:
        x = 'C'
    else:
        x = 'J'
    if resY['B']>=resY['C'] and resY['B']>=resY['J']:
        y = 'B'
    elif resY['C']>=resY['J']:
        y = 'C'
    else:
        y = 'J'
    return (x,y)
@performance('s')
def main():
    resX = {'B':0, 'C':0, 'J':0}
    resY = {'B':0, 'C':0, 'J':0}
    sys.stdin = open('./1.txt', 'r')
    n = input()
    for i in xrange(n):
        A = sys.stdin.readline()
        if A=='B C\n':
            resX['B'] += 1
        elif A=='B J\n':
            resY['J'] += 1
        elif A=='C J\n':
            resX['C'] += 1
        elif A=='C B\n':
            resY['B'] += 1
        elif A=='J B\n':
            resX['J'] += 1
        elif A=='J C\n':
            resY['C'] += 1
    XW = resX['B']+resX['C']+resX['J']
    XL = resY['B']+resY['C']+resY['J']
    TIE = n - XW - XL
    print XW, TIE, XL
    print XL, TIE, XW
    x, y = most(resX, resY)
    print x, y
    

if __name__ == '__main__':
    main()
