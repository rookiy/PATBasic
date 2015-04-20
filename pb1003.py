#!/usr/bin/env python
import sys
import re

Pattern = re.compile(r'(?P<n1>A*)P(?P<n2>A+)T(?P<n3>A*)')

def match(string):
    tmp = Pattern.match(string)
    if tmp:
        n1, n2, n3 = map(len, tmp.groups())
        if n3 == n1*n2:
            return True
    return False

def main():
    #sys.stdin = open('./1.txt','r')
    n = input()
    for i in range(n):
        string = raw_input()
        result = match(string)
        if result:
            print 'YES'
        else:
            print 'NO'
        

if __name__ == '__main__':
    main()
