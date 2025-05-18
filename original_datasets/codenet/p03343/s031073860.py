from sys import exit, setrecursionlimit, stderr
from functools import reduce
from itertools import *
from collections import *
from bisect import *

def read():
  return int(input())
 
def reads():
  return [int(x) for x in input().split()]

INF = 1 << 60

N, K, Q = reads()
A = reads()

A.append(-INF)
def getlub(y):
  v = []
  l = 0
  for i in range(N+1):
    if A[i] < y:
      w = A[l:i]
      w.sort()
      if len(w) >= K-1:
        v.extend(w[:len(w)-K+1])
      l = i + 1
  v.sort()
  return v[Q-1] if len(v) >= Q else INF

ans = INF
for Y in A[:-1]:
  X = getlub(Y)
  ans = min(ans, X - Y)
print(ans)