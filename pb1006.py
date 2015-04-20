#!/usr/bin/env python
import sys

List = []

def generate_list():
    List.append('0')
    for i in range(1,1000):
        string = ''
        for j in range(i/100):
            string += 'B'
        for j in range(i%100/10):
            string += 'S'
        for j in range(1,i%10+1):
            string += str(j)
        List.append(string)

def main():
    #sys.stdin = open('./1.txt', 'r')
    n = input()
    print List[n]

if __name__ == '__main__':
    generate_list()
    main()
