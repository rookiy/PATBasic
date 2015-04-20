#!/usr/bin/env python
import sys

def main():
    sys.stdin = open('./1.txt', 'r')
    N, p = map(int, sys.stdin.readline().split())
    l = map(int, sys.stdin.readline().split())
    l.sort()
    l.append(-1)
    i = 0
    max_num = 0
    while 1:
        start = l[i]
        end = start*p
        for j in range(i+1, N+1):
            if l[j] > end:
                break
        count = j - i
        if count > max_num:
            max_num = count
        if j == N:
            break
        i += 1

    print max_num

if __name__ == '__main__':
    main()

