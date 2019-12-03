#!/bin/python3

import sys


#n = int(input().strip())
#steps = input().upper()

n=8
steps='UDDDUDUU'
level=0
valley=0
above=True

for char in steps :
	if char == 'D':
		level-=1
	else :
		level+=1
	if above and level<0 : 
		above=False
		valley+=1
	elif not above and level==0 : above=True
print(valley)
