#!/usr/bin/env python
import sys

def comp(due, pay):
    c1 = cmp(due[0], pay[0])
    if c1 != 0:
        return c1
    else:
        c2 = cmp(due[1], pay[1])
        if c2 != 0:
            return c2
        else:
            c3 = cmp(due[2], pay[2])
            return c3

def mns(due, pay):
    ans = []
    if due[2] >= pay[2]:
        ans.append(due[2] - pay[2])
    else:
        ans.append(due[2] + 29 - pay[2])
        due[1] -= 1
    if due[1] >= pay[1]:
        ans.insert(0, due[1] - pay[1])
    else:
        ans.insert(0, due[1] + 17 - pay[1])
        due[0] -= 1
    ans.insert(0, due[0] - pay[0])
    return ans

def main():
    sys.stdin = open('./1.txt', 'r')
    due, pay = raw_input().split()
    due = map(int, due.split('.'))
    pay = map(int, pay.split('.'))
    flag = comp(due, pay)
    if flag == -1:
        due, pay = pay, due
    ans = mns(due, pay)
    ans[0] = ans[0] * flag * -1
    print '%d.%d.%d' % (ans[0], ans[1], ans[2])
    
if __name__ == '__main__':
    main()

