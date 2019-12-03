#!/bin/python3

import sys


x1,v1,x2,v2 = input().strip().split(' ')
x1,v1,x2,v2 = [int(x1),int(v1),int(x2),int(v2)]


leader=1 if x1>x2 else 2
print(leader)
while True:
    x1+=v1
    x2+=v2
    new_leader = 1 if x1>x2 else 2
    print(new_leader)
    if new_leader!=leader:
    	print('NO')
    	exit()
    if x1==x2 : 
        print('YES')
        exit()