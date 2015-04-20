#!/usr/bin/env python
import sys

weigh = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]

dic = {0:'1', 1:'0', 2:'X', 3:'9', 4:'8', 5:'7', 6:'6', 7:'5', 8:'4', 9:'3', 10:'2'}

def check(line):
    sum = 0
    for i, w in zip(range(17), weigh):
        if line[i]<'0' or line[i]>'9' :
            return False
        else :
            sum += int(line[i]) * w
    Z = sum % 11
    if dic[Z] == line[17] :
        return True
    else :
        return False

def main():
    wrong = []
    sys.stdin = open('./1.txt', 'r')
    N = input()
    for i in range(N):
        line = raw_input()
        if not check(line) :
            wrong.append(line)
    if len(wrong) == 0 :
        print 'All passed'
    else :
        print '\n'.join(wrong)
        
    
if __name__ == '__main__':
    main()
