#!/usr/bin/env python
import sys

Matrix = []

def generate_matrix():
    for i in range(0,101):
        Matrix.append([])
    for i in range(2,101):
        List = []
        n = i
        while n != 1:
            if n%2 ==0:
                n /= 2
                List.append(n)
            else:
                n = (3*n+1)/2
                List.append(n)
        Matrix[i] = List
                
def dataclean(list):
    tmp = list[:]
    for i in list:
        if i in tmp:
            for j in Matrix[i]:
                if j in tmp:
                    tmp.remove(j)
    tmp.sort(reverse=True)
    return tmp

def main():
    #sys.stdin = open('./1.txt', 'r')
    n = input()
    list = [int(i) for i in raw_input().split()]
    tmp = dataclean(list)
    sys.stdout.write(str(tmp[0]))
    for (index,item) in enumerate(tmp):
        if index==0:
            continue
        sys.stdout.write(' '+str(item))
    

if __name__ == '__main__':
    generate_matrix()
    main()