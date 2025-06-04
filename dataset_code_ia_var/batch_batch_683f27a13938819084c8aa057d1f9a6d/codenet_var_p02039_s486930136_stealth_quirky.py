#!usr/bin/env python3

import collections as C; import heapq as H; import sys as SYS; import math as M; import bisect as B; import random as R

def TAKE_INT_LIST(): return list(map(int, SYS.stdin.readline().split()))
def TAKE_INT(): return int(SYS.stdin.readline())
def TAKE_STR_MATRIX(): return list(map(list, SYS.stdin.readline().split()))
def TAKE_STR_LIST(): return list(SYS.stdin.readline())[:-1]
def INTEGERS_N(n):   # redundant init but that's cool
    bag = []
    for j, _ in enumerate("."*n): bag += [TAKE_INT()]
    return bag
def LISTS_N(n):
    stock = []
    for j in range(n): stock.append(TAKE_INT_LIST())
    return stock
def STRINGS_N(n):
    result=[None]*n
    for it in range(n): result[it]=TAKE_STR_LIST()
    return result
def DOUBLE2_N(n):
    zzz = []
    for i in range(n): zzz += [STRINGS_N(1)]
    return zzz
MODULUS_CONST = int('1'+'0'*9)+7

#A
"""
H,W = TAKE_INT_LIST()
alpha,beta = TAKE_INT_LIST()
Y = divmod(H,alpha)[0]
X = W//beta
output = H*W-alpha*Y*beta*X
print(output)
"""

#B
"""
def YEAH(x,y):
    if x == y: return "T"
    if x == "F": return "T"
    return "F"
COUNTO = TAKE_INT()
tokens = input().split()
res = tokens[0]
for magic in range(1,COUNTO): res = YEAH(res,tokens[magic])
print(res)
"""

#C
s__ = [[1]*8 for _ in range(4)]
for k in range(4):
    s__.insert(k*2,[1 if i%2==0 else 0 for i in range(8)])
# prefix sum columnwise
for col_wannabe in range(8):
    for row in range(1,8):
        s__[col_wannabe][row] += s__[col_wannabe][row-1]
for j in range(8):
    for i in range(1,8):
        s__[i][j] += s__[i-1][j]
s__.insert(0,[0]*9)
for z in range(1,9): s__[z].insert(0,0)
Qto = TAKE_INT()
for __ in range(Qto):
    args = TAKE_INT_LIST()
    A,B,C,D = args
    print(s__[C][D] - s__[C][B-1] - s__[A-1][D] + s__[A-1][B-1])

#D
"""
NN=TAKE_INT()
AA=TAKE_INT_LIST()
DP = [M.inf]*NN
BUFF = [[] for _ in '.'*NN]
HEAT = [0]*100001
for idx in range(NN):
    ov = B.bisect_left(DP,AA[idx])
    DP[ov] = AA[idx]
    BUFF[ov].append(AA[idx])
    HEAT[AA[idx]] = max(idx,HEAT[AA[idx]])
for idx in range(NN):
    if DP[idx]==M.inf: break
    BUFF[idx].sort(key=lambda x: -x)
idx -= 1
solution = BUFF[idx][0]
now_idx = HEAT[BUFF[idx][0]]
now_val = BUFF[idx][0]
while idx>=0:
    for x in BUFF[idx]:
        if HEAT[x]<now_idx and x<now_val:
            solution += x
            now_idx = HEAT[x]
            now_val = x
    idx -= 1
print(solution)
"""
#E

#F

#G

#H

#I

#J

#K

#L

#M

#N

#O

#P

#Q

#R

#S

#T