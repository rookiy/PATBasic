#!/usr/bin/env python
import sys
import re

Pattern = re.compile(r'.*P.*A.*T.*')

def main():
    p = []
    a = []
    t = []
    
    sys.stdin = open('./1.txt', 'r')
    string = raw_input()
    
    for index, char in enumerate(string):
        if char == 'P':
            p.append(index)
        elif char == 'A':
            a.append(index)
        else:
            t.append(index)
    
    count = 0
    
    for i in p:
        for j in a:
            for k in t:
                if i <= j <= k:
                    count += 1
    print count
    
    
if __name__ == '__main__':
    main()
