#!/usr/bin/env python
import sys

dict = {}

def main():
    sys.stdin = open('./1.txt', 'r')
    N = input()
    high = -1
    high_name = ''
    for line in sys.stdin:
        name, score = line.split()
        if name in dict:
            dict[name] += int(score)
        else :
            dict[name] = int(score)
        s = dict[name]
        if s > high:
            high = s
            high_name = name
    
    print high_name, high
        

if __name__ == '__main__':
    main()
