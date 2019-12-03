#!/bin/python

import sys

def solve(arr, money):
    costs = {}
    for i in range(len(arr)):
        costs[str(arr[i])] = i
    #print costs
    for i in range(len(arr)):
        try:
            if costs[str(money - arr[i])] != money :
                print i+1,costs[str(money - arr[i])]+1
                return
        except:
            pass

if __name__ == "__main__":
    t = int(raw_input().strip())
    for a0 in xrange(t):
        money = int(raw_input().strip())
        n = int(raw_input().strip())
        arr = map(int, raw_input().strip().split(' '))
        solve(arr, money)