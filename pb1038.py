#!/usr/bin/env python
import sys

dic = {}

def main():
    sys.stdin = open('./1.txt', 'r')
    N = input()
    for item in raw_input().split():
        if item in dic:
            dic[item] += 1
        else:
            dic[item] = 1
    Klist = raw_input().split()[1:]
    for item in Klist[:-1]:
        if item in dic:
            sys.stdout.write(str(dic[item]) + ' ')
        else:
            sys.stdout.write('0 ')
    item = Klist[-1]
    if item in dic:
        print dic[item]
    else:
        print '0'
if __name__ == '__main__':
    main()
