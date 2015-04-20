#!/usr/bin/env python
import sys

def main():
    sys.stdin = open('./1.txt', 'r')
    L = map(int, raw_input().split())
    Ans = ''
    for (index,i) in enumerate(L):
        if index == 0:
            continue
        if i!=0:
            L[index] -= 1
            Ans = str(index)
            break
    for (index,i) in enumerate(L):
        if i!=0:
            Ans += str(index)*i
    print Ans

if __name__ == '__main__':
    main()
