import math
import string
import itertools as it
import fractions as fr
import heapq
import collections
import re
import array
import bisect as bs
import sys,random
import time
import copy
from functools import reduce

sys.setrecursionlimit(int(1e7))
inf = 1e20
eps = 1.0 / 1e10
mod = 998244353
DIRS4 = [[0,-1],[1,0],[0,1],[-1,0]]
DIRS8 = [(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,-1),(-1,0),(-1,1)]

def li():
  return list(map(int, sys.stdin.readline().split()))
def li_():
  return [int(x)-1 for x in sys.stdin.readline().split()]
def lf():
  return list(map(float, sys.stdin.readline().split()))
def ls():
  return sys.stdin.readline().split()
I=lambda: int(sys.stdin.readline())
F=lambda: float(sys.stdin.readline())
def S():
  return input()
def PF(x):
  print(x,flush=True)

def main():
  AnswerList = []

  digits = string.digits
  letters = string.ascii_uppercase
  symbols = digits + letters

  while 1:
    try:
      n,m,q = li()
    except:
      break
    if n==0:
      break

    arr = []
    for __ in range(q): arr.append(ls())
    if n==1:
      AnswerList += ['0'*m]
      continue

    u=[0]*m; v=[0 for _ in range(m)]
    curr = 0
    allbits = pow(2,n)-1

    for t,s in arr:
      mt = int(''.join(reversed(t)),2)
      tu = curr ^ mt
      tv = allbits ^ tu
      for idx,item in enumerate(s):
        if item=='1':
          u[idx] |= tu
          v[idx] |= tv
        else:
          v[idx] |= tu
          u[idx] |= tv
      curr = tu

    out = ""
    for i in range(m):
      val = None
      for ti in range(n):
        if ((u[i]&(1<<ti)) and not (v[i]&(1<<ti))):
          if val is None:
            val = symbols[ti]
          else:
            val = '?'
            break
      out += str(val) if val is not None else '?'
    AnswerList.append(out)

  return '\n'.join(map(str, AnswerList))

if __name__=='__main__':
  print(main())