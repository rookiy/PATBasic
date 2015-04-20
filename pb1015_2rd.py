#!/usr/bin/env python
import sys
from decorator4 import performance
from ctypes import CDLL

def rank(x, y):
    con1 = cmp(x[1]+x[2],y[1]+y[2])
    if con1 != 0:
        return con1*-1
    else:
        con2 = cmp(x[1], y[1])
        if con2 != 0:
            return con2*-1
        else:
            return cmp(x[0], y[0])
@performance('s')
def main():
    A, B, C, D = [], [], [], []
    sys.stdin = open('./1.txt', 'r')
    msv = CDLL('msvcrt.dll')
    N, L, H = map(int, sys.stdin.readline().split())
    for line in sys.stdin.readlines():
        stuid, score1, score2 = map(int, line.split())
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
    '''
    A.extend(B)
    A.extend(C)
    A.extend(D)
    Ans = ['%d %d %d'%(i[0],i[1],i[1]) for i in A]
    sys.stdout.write('\n'.join(Ans))
    '''
    for item in A:
        #sys.stdout.write(' '.join(map(str,item))+"\n")
        #sys.stdout.write('%d %d %d\n'%(item[0],item[1],item[2]))
        #print '%d %d %d'%(item[0],item[1],item[2])
        msv.printf(' '.join(map(str,item))+"\n")
    
    for item in B:
        #sys.stdout.write(' '.join(map(str,item))+"\n")
        #sys.stdout.write('%d %d %d\n'%(item[0],item[1],item[2]))
        #print '%d %d %d'%(item[0],item[1],item[2])
        msv.printf(' '.join(map(str,item))+"\n")
    for item in C:
        #sys.stdout.write(' '.join(map(str,item))+"\n")
        #sys.stdout.write('%d %d %d\n'%(item[0],item[1],item[2]))
        #print '%d %d %d'%(item[0],item[1],item[2])
        msv.printf(' '.join(map(str,item))+"\n")
    for item in D:
        #sys.stdout.write(' '.join(map(str,item))+"\n")
        #sys.stdout.write('%d %d %d\n'%(item[0],item[1],item[2]))
        #print '%d %d %d'%(item[0],item[1],item[2])
        msv.printf(' '.join(map(str,item))+"\n")
    msv.fflush(None)
    sys.exit(0)
if __name__ == '__main__':
    main()
