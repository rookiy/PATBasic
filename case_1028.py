#!/usr/bin/env python
import sys
import random

target = open('./1.txt', 'w')

target.write('100000\n')

for i in range(100000):
    target.write('James'+str(i)+' ')
    year = random.randint(1800, 2100)
    month = random.randint(1,12)
    day = random.randint(1,31)
    target.write('%4d/%02d/%02d\n' % (year, month, day))
    if i%5000 == 0:
        print i
