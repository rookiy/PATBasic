#!/usr/bin/env python
import sys
import random

target = open('./1.txt', 'w')

target.write('-1.')

for i in range(10000):
    target.write(str(random.randint(0,9)))

target.write('E-9999')