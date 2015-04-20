#!/usr/bin/env python
import sys
import random

target = open('./1.txt', 'w')

l = ['P', 'A', 'T']

for i in range(100000):
    target.write(random.choice(l))
target.write('\n')