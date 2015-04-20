#!/usr/bin/env python

import sys

class Cake(object):
    def __init__(self, amount, sale):
        self.amount = amount
        self.sale = sale
        # save the precision for case 4
        self.price = sale/amount
        
def main():
    sys.stdin = open('./1.txt', 'r')
    N, D = map(int, raw_input().split())
    # use float instead of int for the number of amount
    # and sale of a cake may not be an integer(case 2)
    Amounts = map(float, raw_input().split())
    Sales = map(float, raw_input().split())
    Cakes = []
    Ans = 0.0
    for i in xrange(N):
        cake = Cake(Amounts[i], Sales[i])
        Cakes.append(cake)
    Cakes.sort(key=lambda i:i.price, reverse=True)
    for cake in Cakes:
        if D>=cake.amount:
            Ans += cake.sale
            D -= cake.amount
        else:
            Ans += D*cake.price
            D = 0
        if D==0:
            break
    print '%.2f'%Ans
    

if __name__ == '__main__':
    main()