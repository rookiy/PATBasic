#!/usr/bin/env python
import sys
import re

def main():
    numT, numAT, numPAT = 0, 0, 0
    
    sys.stdin = open('./1.txt', 'r')
    string = list(raw_input())
    string.reverse()
    
    for char in string:
        if char == 'T':
            numT += 1
        elif char == 'A':
            numAT = (numAT + numT) % 1000000007
        else:
            numPAT = (numPAT + numAT) % 1000000007
    
    print numPAT
    
    
if __name__ == '__main__':
    main()

