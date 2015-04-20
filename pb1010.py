#!/usr/bin/env python
import sys

def deritive(multi):
    for tup in multi:
        tup[0] = tup[0]*tup[1]
        tup[1] -= 1
        if tup[0]==0:
            multi.remove(tup)
    if len(multi)==0:
        multi.append([0,0])

def main():
    sys.stdin = open('./1.txt', 'r')
    tmplist = map(int, raw_input().split())
    multi = [[tmplist[i], tmplist[i+1]] for i in range(0, len(tmplist), 2)]
    deritive(multi)
    for (index,tup) in enumerate(multi):
        if index != len(multi)-1:
            sys.stdout.write(str(tup[0])+' '+str(tup[1])+' ')
        else:
            sys.stdout.write(str(tup[0])+' '+str(tup[1]))


if __name__ == '__main__':
    main()

