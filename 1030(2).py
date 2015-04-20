import sys

sys.stdin = open('./1.txt', 'r')
str1 = raw_input()
str2 = raw_input()

Np = str1.split(' ')
N = int(Np[0])
p = int(Np[1])

strNum = str2.split(' ')
num = []

for i in strNum:
    num.append(int(i))

num.sort()       

start = 0
end = 0
maxLen = 0

while True:

    if start == end:
        end += 1
        continue

    if end >= N:
        break

    if num[end] <= p * num[start]:
        end += 1
    else:
        if maxLen < (end - start):
            maxLen = end - start
        start += 1
    
    if end == N:
        break

if maxLen < end - start:
    maxLen = end - start

print maxLen
