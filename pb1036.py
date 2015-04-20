#!/usr/bin/env python
import sys

def main():
    sys.stdin = open('./1.txt', 'r')
    N, char = raw_input().split()
    column = int(N)
    row = int(round(float(column)/2))
    for i in range(row):
        if i == 0 or i == row-1:
            print char*column
        else:
            print char+' '*(column-2)+char

if __name__ == '__main__':
    main()