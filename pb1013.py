#!/usr/bin/env python
import sys

L = []

def prime():
    tmp = [1 for i in range(0, 110001)]
    for i in range(2,332):
        if tmp[i]==1:
            factor = i
            while factor*i <=110000:
                tmp[factor*i] = 0
                factor += 1
    for i in range(2,110001):
        if tmp[i]==1:
            L.append(i)

def main():
    sys.stdin = open('./1.txt', 'r')
    n, m = map(int, raw_input().split())
    res = L[n-1:m]
    for (index, item) in enumerate(res):
        sys.stdout.write(str(item))
        if index == len(res)-1:
            continue
        if (index+1)%10 == 0:
            sys.stdout.write('\n')
        else:
            sys.stdout.write(' ')

if __name__ == '__main__':
    prime()
    main()
