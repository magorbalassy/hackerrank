#!/bin/python

from __future__ import print_function

import os
import sys

#
# Complete the arrayManipulation function below.
#
def arrayManipulation(n, queries):
    el = [0 for _ in range(n)]
    start=1
    stop=0
    events = sorted(query for r in queries for query in zip(r,(start,stop)))
    maxSeq = 0
    maxEl = 0
    maxIndex = 0
    maxAmount = [0 for _ in range(n)]
    for index, event in events:
        if event == 1 : 
            maxSeq += 1
        else:
            maxSeq -= 1
        if maxEl < maxSeq :
            maxEl = maxSeq
            maxIndex = index
            el[index] = maxIndex
        #print ('index:',index,'event:',event)
    #print('max items:',maxEl)
    #print(el[-100:])
    temp = 0
    el.sort()
    print(el[-100:])
    for e in el[-50:] :
        for s1, s2, amount in queries:
            if s1 <= e <= s2:
                maxAmount[e] += amount
    return [m for m in maxAmount if m != 0 ]

if __name__ == '__main__':

    nm = raw_input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in xrange(m):
        queries.append(map(int, raw_input().rstrip().split()))

    result = arrayManipulation(n, queries)

    print(result)
    #print ([r for r in result if r != 0])
