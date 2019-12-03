#!/bin/python

import sys

def solve(arr, money):

    #in this case the index numbers will change because of the sort
    arr.sort()
    lo = 0
    hi = len(arr)-1
    while lo<hi:
        if arr[lo] + arr[hi] > money:
            hi -= 1
        elif arr[lo] + arr[hi] < money:
            lo += 1
        elif arr[lo] + arr[hi] == money:
            print lo+1, hi+1
            return

if __name__ == "__main__":
    t = int(raw_input().strip())
    for a0 in xrange(t):
        money = int(raw_input().strip())
        n = int(raw_input().strip())
        arr = map(int, raw_input().strip().split(' '))
        solve(arr, money)