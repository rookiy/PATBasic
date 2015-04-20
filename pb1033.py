#!/usr/bin/env python
import sys

UpperAlpha = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

def main():
    Ans = []
    sys.stdin = open('./1.txt', 'r')
    
    text1 = raw_input()
    broken = set(text1)
    for item in text1:
        if item.isalpha() :
            broken.add(item.lower())
    if '+' in broken :
        broken = broken.union(UpperAlpha)
    
    text = raw_input()
    for char in text:
        if char in broken :
            continue
        Ans.append(char)
    
    print ''.join(Ans)

if __name__ == '__main__':
    main()
