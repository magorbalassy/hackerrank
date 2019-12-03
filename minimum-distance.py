#!/bin/python3

import sys


#n = int(input().strip())
#A = [int(A_temp) for A_temp in input().strip().split(' ')]
n=6
A=[7,1,3,4,1,7]
dist=n
for i in range(n):
    for j in range(i+1,n):
    	if (A[i]==A[j]):
        	if abs(i-j)<dist : dist=abs(i-j)
print(dist)