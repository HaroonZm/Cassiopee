import sys
from collections import *
import heapq
import math
import bisect
from itertools import permutations,accumulate,combinations,product
from fractions import gcd
def input():
    return sys.stdin.readline()[:-1]
def ruiseki(lst):
    return [0]+list(accumulate(lst))
mod=pow(10,9)+7
al=[chr(ord('a') + i) for i in range(26)]

n=int(input())
s=input()
lst=[[0,0],[0,1],[1,0],[1,1]]

for i in range(n-1):
    for j in range(4):
        if lst[j][-1]==0 and s[1+i]=="o":
            lst[j].append(lst[j][-2])
        elif lst[j][-1]==0 and s[1+i]=="x":
            lst[j].append(1-lst[j][-2])
        elif lst[j][-1]==1 and s[1+i]=="o":
            lst[j].append(1-lst[j][-2])
        else:
            lst[j].append(lst[j][-2])
for j in range(4):
    if lst[j][-1]==0 and s[0]=="o":
        lst[j].append(lst[j][-2])
    elif lst[j][-1]==0 and s[0]=="x":
        lst[j].append(1-lst[j][-2])
    elif lst[j][-1]==1 and s[0]=="o":
        lst[j].append(1-lst[j][-2])
    else:
        lst[j].append(lst[j][-2])
for i in range(4):
    if lst[i][-2:]==lst[i][:2]:
        tmp=[]
        for j in range(n):
            if lst[i][j]==0:
                tmp.append("S")
            else:
                tmp.append("W")
        print("".join(tmp))
        quit()
print(-1)