#!/usr/bin/env python
import sys
import random

target = open('./1.txt', 'w')

target.write('100000 1000\n')

for i in range(1,100000):
    target.write(str(random.randint(1,1000000000)) + ' ')
target.write(str(random.randint(1,1000000000)) + '\n')
