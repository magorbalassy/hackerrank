#!/bin/python3

import sys


n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]
n,k=6,3
a=[1,3,2,6,1,2]
score=0
for i in range(n):
    for j in range(i+1,n):
    	if ((a[i]+a[j])%k==0):
        	score+=1
print(score)