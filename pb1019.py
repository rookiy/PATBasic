#!/usr/bin/env python
import sys

def twonum(num):
    x = sorted(num, reverse = True)
    y = sorted(num)
    return (''.join(x), ''.join(y))

def main():
    sys.stdin = open('./1.txt', 'r')
    n = '%04d'%(input())
    while 1:
        x, y = map(int, twonum(n))
        print '%04d - %04d = %04d' % (x, y , x-y)
        n = '%04d'%(x-y)
        if n == '6174' or n == '0000':
            break

if __name__ == '__main__':
    main()


