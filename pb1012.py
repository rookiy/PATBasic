#!/usr/bin/env python
import sys

A1, A2, A3, A4, A5 = [],[],[],[],[]

def process(List):
    res = []
    for i in List:
        if i%10==0:
            A1.append(i)
        elif i%5==1:
            A2.append(i)
        elif i%5==2:
            A3.append(i)
        elif i%5==3:
            A4.append(i)
        elif i%5==4:
            A5.append(i)
    if len(A1) == 0:
        res.append('N')
    else:
        res.append(str(reduce(lambda x,y:x+y, A1)))
    if len(A2) == 0:
        res.append('N')
    else:
        sum = 0
        for (index, item) in enumerate(A2):
            if index%2 == 0:
                sum += item
            else:
                sum -= item
        res.append(str(sum))
    if len(A3) == 0:
        res.append('N')
    else:
        res.append(str(len(A3)))
    if len(A4) == 0:
        res.append('N')
    else:
        sum = reduce(lambda x,y:x+y, A4)
        avg = round(float(sum)/len(A4), 1)
        res.append(str(avg))
    if len(A5) == 0:
        res.append('N')
    else:
        A5.sort(reverse=True)
        res.append(str(A5[0]))
    return res

def main():
    sys.stdin = open('./1.txt', 'r')
    tmp = map(int, raw_input().split())
    List = tmp[1:]
    res = process(List)
    sys.stdout.write(res[0])
    for (index, item) in enumerate(res):
        if index == 0:
            continue
        sys.stdout.write(' '+item)
    
if __name__ == '__main__':
    main()
