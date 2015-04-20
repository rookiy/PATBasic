#!/usr/bin/env python
import sys
import re

Pattern = re.compile(r'(\d+)/(\d+)/(\d+)')
l = []

'''
   one case return not zero, one case out of time
   try not to sort the list, just record who is yongest who is oldest
'''

def sort(x, y):
    cmp_year = cmp(x[1], y[1])
    if cmp_year != 0:
        return cmp_year
    else:
        cmp_month = cmp(x[2], y[2])
        if cmp_month != 0:
            return cmp_month
        else:
            return cmp(x[3], y[3])

def main():
    sys.stdin = open('./1.txt', 'r')
    N = input()
    for i in xrange(N):
        name, birthstr = raw_input().split()
        match = Pattern.match(birthstr)
        year, month, day = map(int, match.groups())
        if year>2014 or (year==2014 and month>9) or (year==2014 and month==9 and day>6):
            continue
        if year<1814 or (year==1814 and month<9) or (year==1814 and month==9 and day<6):
            continue
        l.append([name,year,month,day])
    l.sort(sort)
    print len(l), l[0][0], l[-1][0]
        

if __name__ == '__main__':
    main()
