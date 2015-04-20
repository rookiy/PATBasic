#!/usr/bin/env python
import sys

def main():
    sys.stdin = open('./1.txt', 'r')
    A, Da, B, Db = raw_input().split()
    da, db = int(Da), int(Db)
    Pa, Pb = 0, 0 
    for i in A:
        if i == Da:
            Pa *= 10
            Pa += da
    for i in B:
        if i == Db:
            Pb *= 10
            Pb += db
    print Pa+Pb 
            

if __name__ == '__main__':
    main()