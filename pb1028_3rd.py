#!/usr/bin/env python
import sys

def main():
    sys.stdin = open('./1.txt', 'r')
    
    N = input()
    
    count = 0
    youngname = ''
    youngage = '1814/09/05'
    oldname = ''
    oldage = '2014/09/07'
    for line in sys.stdin.readlines():
        name, birthstr = line.split()
        if birthstr>'2014/09/06' or birthstr<'1814/09/06':
            continue
        count += 1
        if birthstr > youngage :
            youngname = name
            youngage = birthstr
        if birthstr < oldage :
            oldname = name
            oldage = birthstr
    if count != 0:
        print count, oldname, youngname
    else:
        print count
        

if __name__ == '__main__':
    main()



