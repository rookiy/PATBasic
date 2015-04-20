#!/usr/bin/env python
import sys
from decorator4 import performance
Students, A, B, C, D = [], [], [], [], []

def rank(x, y):
    if cmp(x[1]+x[2],y[1]+y[2]) != 0:
        return -cmp(x[1]+x[2],y[1]+y[2])
    else:
        if cmp(x[1], y[1])!=0:
            return -cmp(x[1], y[1])
        else:
            return cmp(x[0], y[0])

def Partition(StudentsIn, H):
    for stu in StudentsIn:
        if stu[1]>=H and stu[2]>=H:
            A.append(stu)
        elif stu[1]>=H:
            B.append(stu)
        elif stu[1]>=stu[2]:
            C.append(stu)
        else:
            D.append(stu)
    A.sort(rank)
    B.sort(rank)
    C.sort(rank)
    D.sort(rank)

@performance('s')
def main():
    N, L, H = map(int, raw_input().split())
    for i in range(N):
        Students.append(map(int, raw_input().split()))
    StudentsIn = filter(lambda x: x[1]>=L and x[2]>=L, Students)
    Partition(StudentsIn, H)
    print len(StudentsIn)
    for item in A:
        print ' '.join(map(str, item))
    for item in B:
        print ' '.join(map(str, item))
    for item in C:
        print ' '.join(map(str, item))
    for item in D:
        print ' '.join(map(str, item))

if __name__ == '__main__':
    main()
