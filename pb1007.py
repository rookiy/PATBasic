#!/usr/bin/env python
import sys

List = [1 for i in range(100000)]

def prime():
    for i in range(2,317):
        if List[i] == 1:
            factor = i
            while factor*i < 100000:
                List[factor*i] = 0
                factor += 1
    
def main():
    #sys.stdin = open('./1.txt', 'r')
    n = input()
    count = 0 
    for i in range(3,n-1,2):
        if List[i]==1 and List[i+2]==1:
            count += 1
    print count

if __name__ == '__main__':
    prime()
    main()
