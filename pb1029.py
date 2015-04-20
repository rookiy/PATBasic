#!/usr/bin/env python
import sys



def main():
    sys.stdin = open('./1.txt', 'r')
    missing = []
    original = raw_input()
    broken = raw_input()
    end1 = len(original)
    end2 = len(broken)
    i, j = 0, 0
    while 1:
        if original[i] == broken[j]:
            i += 1
            j += 1
        else:
            missing.append(original[i])
            i += 1
        if j == end2:
            break
    for k in range(i, end1):
        missing.append(original[i])
    whole = ''.join(missing).upper()
    out = []
    for char in whole:
        if char not in out:
            out.append(char)
    print ''.join(out)

if __name__ == '__main__':
    main()
