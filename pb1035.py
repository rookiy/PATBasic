#!/usr/bin/env python
import sys

def merge(l, start, mid, end):
    aux = l[:]
    i, j = start, mid+1
    for k in range(start, end+1):
        if i > mid:
            l[k] = aux[j]
            j += 1
        elif j > end:
            l[k] = aux[i]
            i += 1
        elif aux[i] < aux[j]:
            l[k] = aux[i]
            i += 1
        else:
            l[k] = aux[j]
            j += 1

def main():
    sys.stdin = open('./1.txt', 'r')
    N = input()
    original = map(int, raw_input().split())
    tmp = map(int, raw_input().split())
    
    N = len(original)
    flag = False
    
    insertsort = original[:]
    for i in range(1, N):
        j = i
        while j > 0 and insertsort[i] < insertsort[j-1]:
            j -= 1
        if insertsort == tmp:
            print 'Insertion Sort'
            flag = True
        if i != j:
            value = insertsort.pop(i)
            insertsort.insert(j, value)
        if flag :
            print ' '.join(map(str, insertsort))
            break
    flag = False
    sz = 1
    mergesort = original[:]
    while sz < N:
        if mergesort == tmp:
            print 'Merge Sort'
            flag = True
        for start in range(0, N-sz, 2*sz):
            end = start+sz+sz-1
            if end > N-1:
                end = N-1 
            merge(mergesort, start, start+sz-1, end)
        if flag:
            print ' '.join(map(str,mergesort))
            break
        sz *= 2    
    
if __name__ == '__main__':
    main()
