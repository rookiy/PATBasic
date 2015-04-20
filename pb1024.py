#!/usr/bin/env python
import sys
import re

Pattern = re.compile(r'([+-])([0-9\.]+)E([+-])([0-9]+)')

def main():
    sys.stdin = open('./1.txt', 'r')
    sci = raw_input()
    match = Pattern.match(sci)
    if match.group(1)=='+':
        flag = 1
    else:
        flag = -1
    if match.group(3)=='+':
        exp = int(match.group(4))
    else:
        exp = int(match.group(4))*-1
    numstr = match.group(2)
    pos = numstr.find('.')
    exp = pos-len(numstr)+1+exp
    l = []
    for i in numstr:
        if i != '.':
            l.append(i)
    numstr = l
    if exp>=0:
        print flag*int(''.join(numstr)+'0'*exp)
    elif exp+len(numstr)>0:
        numstr.insert(exp+len(numstr), '.')
        if flag == -1:
            numstr.insert(0,'-')
        print "".join(numstr)
    else:
        tmp = exp+len(numstr)
        ans = '0.'+'0'*(tmp*-1)
        if flag == -1:
            ans = '-'+ans
        print ans+''.join(numstr)
    
if __name__ == '__main__':
    main()
