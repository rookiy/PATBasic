#!/usr/bin/env python
import sys
import random

target = open('./1.txt', 'w')

target.write('100000\n')

Set = ['B', 'C', 'J']

for i in xrange(100000):
    target.write(random.choice(Set)+' '+random.choice(Set)+'\n')
