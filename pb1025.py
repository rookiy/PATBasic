#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys

d = {}
l = []
'''
    case 1 and case 2 WA, 反转链表时，一组
    Node最后一个输出的下一个节点的地址没有、
    更新为下一组反转后的地址，导致错误
    
    case 5 286ms<300ms
'''
def main():
    sys.stdin = open('./1.txt', 'r')
    Saddr, N, K = raw_input().split()
    N, K = int(N), int(K)
    
    for i in xrange(N):
        tmp = raw_input().split()
        d[tmp[0]] = [tmp[0], tmp[1], tmp[2]]
    
    while Saddr != '-1':
        Node = d[Saddr]
        l.append(Node)
        Saddr = Node[2]
    
    length = len(l)
    k = K-1
    start = True
    for i in xrange(0,length,K):
        if length - i < K:
            sys.stdout.write(l[i][0]+'\n')
            for j in range(length-i):
                print ' '.join(l[i+j])
        else:
            while 1:
                if start:
                    Node = l[i + k]
                    sys.stdout.write(Node[0] + ' ' + Node[1] + ' ')
                    k -= 1
                    start = False
                else:
                    Node = l[i+k]
                    sys.stdout.write(Node[0] + '\n')
                    sys.stdout.write(Node[0] + ' ' + Node[1] + ' ')
                    k -= 1
                if k == -1:
                    k = K-1
                    break
    if length%K == 0:
        sys.stdout.write('-1\n')       

if __name__ == '__main__':
    main()

