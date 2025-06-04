#!/usr/bin/env python3
import sys as _s
import math as m, bisect as b, random
from collections import defaultdict as dd
from collections import deque
from heapq import *
from operator import mul as _m

def LI():
  return list(map(int, _s.stdin.readline().split()))
def I():
  return int(_s.stdin.readline())
def LS():
  return list(map(list, _s.stdin.readline().split()))
def S():
  return list(_s.stdin.readline())[:-1]
def IR(n):
  x = [None] * n
  for i in range(n):
    x[i] = I()
  return x
def LIR(n):
  l = []
  for _ in range(n):
    l.append(LI())
  return l
def SR(n): 
  return [S() for _ in range(n)]
def LSR(n):
  L = []
  for _ in range(n): L.append(LS())
  return L

_s.setrecursionlimit(10**6)
mod = 10 ** 9 + 7

def A():
  def pwin(s, i):
    if s[i] == "[":
      idx = i+1
      w1, idx = pwin(s, idx)
      idx += 1
      w2, idx = pwin(s, idx)
      return res(w1, w2), idx+1
    else:
      return s[i], i+1

  def res(w1, w2):
    if facts[w1]==0:
      if facts[w2]==0:
        return "0"
      else:
        facts[w2] -= 1
        return w2
    else:
      if facts[w2]!=0:
        return "0"
      else:
        facts[w1] -= 1
        return w1

  data = S()
  total = sum(1 for ch in data if ch not in "[-]")
  facts = dd(int)
  facts["0"] = 100000
  for _ in range(total):
    a, b = input().split()
    facts[a] = int(b)
  winner = pwin(data, 0)[0]
  print("No" if facts[winner] else "Yes")
  return

def B():
  n, k = LI()
  s, t = S(), S()
  from collections import deque as dq
  q = dq([])
  r = 0
  for i in range(n):
    if (s[i], t[i]) == ("B", "W"):
      if q:
        popx = q.popleft()
        if i-popx >= k:
          r += 1
          q.clear()
      q.append(i)
  if q: r+=1
  for i in range(n):
    if (s[i], t[i]) == ("W", "B"):
      if q:
        popx = q.popleft()
        if i-popx >= k:
          r+=1
          q.clear()
      q.append(i)
  if q: r+=1
  print(r)
  return

def C():
  n = I()
  s = SR(n)
  t = S()
  # Not implemented
  return

def D():
  def dot(a,b): return sum(map(_m,a,b))
  def mulmat(a,b,mm):
    tb = list(zip(*b))
    return [[dot(r,c)%mm for c in tb] for r in a]
  def matpow(a, exp, mm):
    h = len(a)
    ident = [ [int(i==j) for j in range(h)] for i in range(h)]
    while exp:
      if exp&1: ident = mulmat(ident,a,mm)
      a = mulmat(a,a,mm)
      exp >>= 1
    return ident
  while True:
    vals = LI()
    if vals[0] == 0: break
    n,m,a,b,c,t = vals
    si = LI()
    s2 = [[si[i]] for i in range(n)]
    mat = [ [0]*n for _ in range(n)]
    mat[0][0] = b; mat[0][1] = c
    for idx in range(1, n-1):
      mat[idx][idx-1] = a
      mat[idx][idx] = b
      mat[idx][idx+1] = c
    mat[n-1][-2]=a; mat[n-1][-1]=b
    mat = matpow(mat, t, m)
    mat = mulmat(mat, s2, m)
    print(*[mat[i][0] for i in range(n)])
  return

def E():
  def surf(x,y,z): 
    return ((x==0)|(x==a-1))+((y==0)|(y==b-1))+((z==0)|(z==c-1))+kk
  dirz = ((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1))
  a,b,c,n = LI()
  surfct = [0]*7
  kk = (a==1)+(b==1)+(c==1)
  if not kk:
    surfct[1]=2*(max(0,a-2)*max(0,b-2)+max(0,c-2)*max(0,b-2)+max(0,a-2)*max(0,c-2))
    surfct[2]=4*(max(0,a-2)+max(0,b-2)+max(0,c-2))
    surfct[3]=8
  elif kk==1:
    surfct[2]=max(0,a-2)*max(0,b-2)+max(0,c-2)*max(0,b-2)+max(0,a-2)*max(0,c-2)
    surfct[3]=2*(max(0,a-2)+max(0,b-2)+max(0,c-2))
    surfct[4]=4
  elif kk==2:
    surfct[4]=max(0,a-2)+max(0,b-2)+max(0,c-2)
    surfct[5]=2
  else:
    surfct[6]=1
  ddct = dd(int)
  for _ in range(n):
    x,y,z = LI()
    surfct[surf(x,y,z)] -= 1
    ddct[(x,y,z)] = -1
    for dx,dy,dz in dirz:
      key = (x+dx,y+dy,z+dz)
      if ddct[key] != -1: ddct[key] += 1
  ans = 0
  for key,val in ddct.items():
    if val!= -1:
      x,y,z = key
      if 0<=x<a and 0<=y<b and 0<=z<c:
        ans += val+surf(x,y,z)
        surfct[surf(x,y,z)] -= 1
  for i in range(1,7):
    ans += i*surfct[i]
  print(ans)
  return

def F(): pass
def G(): pass
def H(): pass
def I_(): pass
def J(): pass

if __name__ == "__main__":
  A()