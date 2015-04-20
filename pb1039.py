#!/usr/bin/env python
import sys

def main():
    sys.stdin = open('./1.txt', 'r')
    stock = list(raw_input())
    want = raw_input()
    count = 0
    for i in want:
        if i in stock :
            count += 1
            stock.remove(i)
    if count == len(want) :
        print 'Yes', len(stock)
    else :
        print 'No', len(want) - count

if __name__ == '__main__':
    main()
