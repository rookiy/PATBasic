#!/usr/bin/env python
import sys

def divide(A, B):
    Q, R = 0, 0
    for i in A:
        R = R*10 + i
        Q = Q*10 + R/B
        R = R%B
    return (Q, R)

def main():
    sys.stdin = open('./1.txt', 'r')
    a, b = raw_input().split()
    B = int(b)
    A = map(int, a)
    q, r = divide(A, B)
    print q, r
        

if __name__ == '__main__':
    main()
