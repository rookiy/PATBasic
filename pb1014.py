#!/usr/bin/env python
import sys

DAY = {'A':'MON', 'B':'TUE', 'C':'WED', 'D':'THU', 'E':'FRI', 'F':'SAT', 'G':'SUN'}
Hour = {'0':'00', '1':'01', '2':'02', '3':'03', '4':'04', '5':'05', '6':'06', '7':'07'
        , '8':'08', '9':'09', 'A':'10', 'B':'11', 'C':'12', 'D':'13', 'E':'14', 'F':'15'
        , 'G':'16', 'H':'17', 'I':'18', 'J':'19', 'K':'20', 'L':'21', 'M':'22', 'N':'23'}

def same1(a, b):
    if a == b:
        if a>='A' and a<='G':
            return True
    return False

def same2(a, b):
    if a == b:
        if a.isdigit() or (a>='A' and a<='N'):
            return True
    return False

def same3(a, b):
    if a == b:
        if a.isalpha():
            return True
    return False

def Format(ans):
    res = ''
    res += DAY[ans[0]]
    res += ' '
    res += Hour[ans[1]]
    res += ':'
    if ans[2]>=0 and ans[2]<=9:
        res +='0'+str(ans[2])
    else:
        res += str(ans[2])
    return res

def main():
    sys.stdin = open('./1.txt', 'r')
    str1 = raw_input()
    str2 = raw_input()
    str3 = raw_input()
    str4 = raw_input()
    flag = True
    index = 0
    ans = []
    for (a, b) in zip(str1, str2):
        if flag:
            if same1(a, b):
                flag = False
                ans.append(a)
        else:
            if same2(a, b):
                ans.append(a)
                # break is important to ensure you only get the first match information
                break
    for (a, b) in zip(str3, str4):
        if same3(a, b):
            ans.append(index)
            break
        index += 1
    res = Format(ans)
    print res

if __name__ == '__main__':
    main()
