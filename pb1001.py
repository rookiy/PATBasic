#!/usr/bin/env python

list = []

def cut(i):
    count = 0
    while i != 1:
        if i%2 == 0:
            i /= 2
            count += 1
        else:
            i = (i*3+1)/2
            count += 1
    return count

def main():
    #raw_input = open('./1.txt','r').readline
    #i, j, k = [int(raw_input()) for i in range(3)]
    i = int(raw_input())
    print list[i-1]

for i in range(1,1001):
    n = cut(i)
    list.append(n)

if __name__ == '__main__':
    main()