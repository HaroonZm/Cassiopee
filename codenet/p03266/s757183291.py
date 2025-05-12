import numpy as np
from functools import reduce
from operator import add,sub,mul,truediv
from fractions import gcd
import itertools 

n,k = map(int,input().split())

x = [0]*k

for i in range(1,n+1):
    x[i%k] = x[i%k]+1

ans = x[0]*x[0]*x[0]

for i in range(1,k):
    b = i%k #決め打ち
    a = (k-b) # 必要なあまりを計算
    c = (k-b) # 必要なあまりを計算
    if((a+c)%k != 0):continue
    ans  = ans + x[a] * x[b] * x[c]

print(ans)