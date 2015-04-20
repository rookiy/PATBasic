#!/usr/bin/env python
import sys

def rotate(L, start, end, axis):
    if axis == 0:
        return
    if (end-start+1)/2 == axis:
        for i in range(end, end-axis, -1):
            tmp = L[i-axis]
            L[i-axis] = L[i]
            L[i] = tmp
    elif (end-start+1)/2 > axis:
        rev_axis = end-start+1-axis
        for i in range(end, end-axis, -1):
            tmp = L[i-rev_axis]
            L[i-rev_axis] = L[i]
            L[i] = tmp
        rotate(L, start+axis, end, axis)
    else:
        rev_axis = end-start+1-axis
        for i in range(end, end-rev_axis, -1):
            tmp = L[i-axis]
            L[i-axis] = L[i]
            L[i] = tmp
        rotate(L, start, end-rev_axis, axis-rev_axis)
            
def main():
    sys.stdin = open('./1.txt', 'r')
    n, m = map(int, raw_input().split())
    L = map(int, raw_input().split())
    rotate(L, 0, n-1, m%n)
    sys.stdout.write(str(L[0]))
    for (index, item) in enumerate(L):
        if index == 0:
            continue
        sys.stdout.write(' '+str(item))

if __name__ == '__main__':
    main()
    
