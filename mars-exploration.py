#!/bin/python3

import sys


S = input().strip()
msg='SOS'
letters=0
for i in range(int(len(S)/3)):
    for j in range(3):
        if S[i*3+j]!=msg[j] : letters+=1
print(letters)