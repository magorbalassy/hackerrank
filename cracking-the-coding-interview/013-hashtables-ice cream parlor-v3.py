#!/bin/python

import sys

def solve(arr, money):
    complement = {}
    for i,el in enumerate(arr):
        if str(el) in complement:
            print complement[str(el)]+1, i+1
        if str(money-el) not in complement :
            complement[str(money - el)] = i
            #print money - el


if __name__ == "__main__":
    t = int(raw_input().strip())
    for a0 in xrange(t):
        money = int(raw_input().strip())
        n = int(raw_input().strip())
        arr = map(int, raw_input().strip().split(' '))
        solve(arr, money)