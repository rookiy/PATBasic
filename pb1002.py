#!/usr/bin/env python

import sys

py = ['ling', 'yi', 'er', 'san', 'si',
      'wu', 'liu', 'qi', 'ba', 'jiu']

def sum(str):
    list = map(int,str)
    value = reduce(lambda x,y:x+y, list)
    return value
        
def main():
    raw_input = open('./1.txt', 'r').readline
    string = raw_input()
    value = sum(string)
    list = map(lambda x:py[int(x)], str(value))
    '''
    sys.stdout.write(list[0])
    for (index,item) in enumerate(list):
        if index == 0:
            continue
        sys.stdout.write(' '+item)
    '''
    print ' '.join(list)

if __name__ == '__main__':
    main()