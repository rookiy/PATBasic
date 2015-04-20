#!/usr/bin/env python
import sys

def main():
    sys.stdin = open('./1.txt', 'r')
    sentence = raw_input().split()
    sentence.reverse()
    sys.stdout.write(sentence[0])
    for (index, item) in enumerate(sentence):
        if index == 0:
            continue
        sys.stdout.write(' '+item)

if __name__ == '__main__':
    main()
