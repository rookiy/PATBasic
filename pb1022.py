#!/usr/bin/env python
import sys

def main():
    sys.stdin = open('./1.txt', 'r')
    A, B, D = map(int, raw_input().split())
    Ans = A + B
    Reminder = []
    while Ans!=0:
        Reminder.insert(0, Ans%D)
        Ans /= D
    # case 3: 0+0
    if len(Reminder)!=0:
        print ''.join(map(str,Reminder))
    else:
        print 0
    

if __name__ == '__main__':
    main()
