#!/usr/bin/env python
import sys

l = []

def generate():
    N = 1
    while 1:
        num = 2 * N * N - 1
        l.append(num)
        if num > 1000:
            break
        N += 1
        
def main():
    sys.stdin = open('./1.txt', 'r')
    total, char = raw_input().split()
    total = int(total)
    N = 1
    for i in range(len(l)):
        if l[i] <= total:
            continue
        N = i
        break
    remaining = total - l[N-1]
    for i in range(N, 0, -1):
        print ' ' * (N-i) + char * (2*i-1)
    for i in range(2, N+1):
        print ' ' * (N-i) + char * (2*i-1)
    print remaining

if __name__ == '__main__':
    generate()
    main()
