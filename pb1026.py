#!/usr/bin/env python
import sys

CLK_TCk = 100

'''
    be care about the precision loss, try not to divide and multiple 
'''

def main():
    sys.stdin = open('./1.txt', 'r')
    C1, C2 = map(int, raw_input().split())
    tik = float(C2 - C1)
    runtime = tik/CLK_TCk
    hour = int(runtime / 3600)
    minute = int(runtime % 3600 / 60)
    second = round(runtime % 60)
    print '%02d:%02d:%02d' % (hour, minute, second)

if __name__ == '__main__':
    main()
