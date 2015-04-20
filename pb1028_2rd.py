#!/usr/bin/env python
import sys
import re

#Pattern = re.compile(r'(\d+)/(\d+)/(\d+)')

def cmp_age(x, y):
    cmp_year = cmp(x[0], y[0])
    if cmp_year != 0:
        return cmp_year
    else:
        cmp_month = cmp(x[1], y[1])
        if cmp_month != 0:
            return cmp_month
        else:
            return cmp(x[2], y[2])

def main():
    sys.stdin = open('./1.txt', 'r')
    
    N = input()
    
    count = 0
    youngname = ''
    yy, ym, yd = 1814, 9, 5
    oldname = ''
    oy, om, od = 2014, 9, 7
    # better than first edition
    for line in sys.stdin.readlines():
        name, birthstr = line.split()
        #match = Pattern.match(birthstr)
        #birth = map(int, match.groups())
        #split is faster than re
        year, month, day = map(int, birthstr.split('/'))
        '''
        if cmp_age(birth, now) == 1:
            continue
        if cmp_age(birth, past) == -1:
            continue
        call function is match slower than use it directly
        '''
        if year>2014 or (year==2014 and month>9) or (year==2014 and month==9 and day>6):
            continue
        if year<1814 or (year==1814 and month<9) or (year==1814 and month==9 and day<6):
            continue
        count += 1
        if year>yy or (year==yy and month>ym) or (year==yy and month==ym and day>yd) :
            youngname = name
            yy, ym, yd = year, month, day
        if year<oy or (year==oy and month<om) or (year==oy and month==om and day<od) :
            oldname = name
            oy, om, od = year, month, day
    if count != 0:        
        print count, oldname, youngname
    else:
        print count
        

if __name__ == '__main__':
    main()


