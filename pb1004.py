#!/usr/bin/env python
import sys
import re

Pattern = re.compile(r'(\w{1,10}) (\w{1,10}) (\d{1,3})')

def match(string):
    res = Pattern.match(string)
    name = res.group(1)
    id = res.group(2)
    score = int(res.group(3))
    tup = (name, id, score)
    return tup

def main():
    #sys.stdin = open('./1.txt', 'r')
    n = input()
    List = []
    for i in range(n):
        string = raw_input()
        tup = match(string)
        List.append(tup)
    List = sorted(List,key=lambda x:x[2],reverse=True)
    print List[0][0], List[0][1]
    print List[-1][0], List[-1][1]

if __name__ == '__main__':
    main()
