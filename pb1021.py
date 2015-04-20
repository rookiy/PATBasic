#!/usr/bin/env python
import sys

occur = [0 for i in range(10)]

def main():
    sys.stdin = open('./1.txt', 'r')
    num = raw_input()
    for i in num:
            occur[int(i)] += 1
    for (index,item) in enumerate(occur):
        if item != 0:
            print '%d:%d'%(index,item)
            

if __name__ == '__main__':
    main()
