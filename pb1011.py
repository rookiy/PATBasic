#!/usr/bin/env python
import sys

def judge(A, B, C):
    if A+B > C:
        return True
    else:
        return False

def main():
    sys.stdin = open('./1.txt', 'r')
    n = input()
    for i in range(1,n+1):
        A,B,C = map(long, raw_input().split())
        res = judge(A, B, C)
        if res:
            print 'Case #'+str(i)+': true'
        else:
            print 'Case #'+str(i)+': false'

if __name__ == '__main__':
    main()