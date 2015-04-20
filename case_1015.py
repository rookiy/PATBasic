#!/usr/bin/env python
import random

target = open('./1.txt','w')
stuid = [i for i in range(10000001, 10110000)]

target.write('100000 60 80\n')

for i in xrange(100000):
    if i%5000 == 0:
        print i
    tmpid = random.choice(stuid)
    stuid.remove(tmpid)
    stuscore1 = random.randint(0,100)
    if stuscore1 < 60:
        stuscore1 = random.randint(0,100)
    stuscore2 = random.randint(0,100)
    if stuscore2 < 60:
        stuscore2 = random.randint(0,100)
    stu = [str(tmpid), str(stuscore1), str(stuscore2)]
    target.write(' '.join(stu))
    target.write('\n')
