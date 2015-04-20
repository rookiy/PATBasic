#!/usr/bin/env python
import sys
from ctypes import CDLL

def rank(x, y):
    con1 = y[1] + y[2] - x[1] - x[2]
    if con1 != 0:
        return con1
    else:
        con2 = y[1] - x[1]
        if con2 != 0:
            return con2
        else:
            return x[0] - y[0]

def main():
    A, B, C, D = [], [], [], []
    sys.stdin = open('./1.txt', 'r')
    msv = CDLL('msvcrt.dll')
    N, L, H = map(int, sys.stdin.readline().split())
    for line in sys.stdin.readlines():
        stuid, score1, score2 = map(int, line.split())
        #stuid, score1, score2 = [int(i) for i in line.split()]
        if score1>=L and score2>=L:
            if score1>=H and score2>=H:
                A.append((stuid, score1, score2))
            elif score1>=H:
                B.append((stuid, score1, score2))
            elif score1>=score2:
                C.append((stuid, score1, score2))
            else:
                D.append((stuid, score1, score2))
    A.sort(rank)
    B.sort(rank)
    C.sort(rank)
    D.sort(rank)
    print len(A)+len(B)+len(C)+len(D)
    for item in A:
        #msv.printf(' '.join(map(str,item))+"\n")
        #msv.printf('%d %d %d\n', item[0], item[1], item[2])
        sys.stdout.write(' '.join(map(str,item))+"\n")
    for item in B:
        #msv.printf(' '.join(map(str,item))+"\n")
        #msv.printf('%d %d %d\n', item[0], item[1], item[2])
        sys.stdout.write(' '.join(map(str,item))+"\n")
    for item in C:
        #msv.printf(' '.join(map(str,item))+"\n")
        #msv.printf('%d %d %d\n', item[0], item[1], item[2])
        sys.stdout.write(' '.join(map(str,item))+"\n")
    for item in D:
        #msv.printf(' '.join(map(str,item))+"\n")
        #msv.printf('%d %d %d\n', item[0], item[1], item[2])
        sys.stdout.write(' '.join(map(str,item))+"\n")

if __name__ == '__main__':
    main()


