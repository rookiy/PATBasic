#!/usr/bin/env python
import sys

def main():
    sys.stdin = open('./1.txt', 'r')
    N, p = map(int, sys.stdin.readline().split())
    l = map(int, sys.stdin.readline().split())
    l.sort()
    
    start = 0
    end = start + 1
    max_num = 1
    
    while end < N :
        if l[end] <= l[start]*p :
            end += 1
        else:
            if end - start > max_num :
                max_num = end - start
            start += 1
    if end - start > max_num :
        max_num = end - start
    
    print max_num

if __name__ == '__main__':
    main()
