#!/usr/bin/env python3
import sys, math, itertools, collections, bisect
input = lambda: sys.stdin.buffer.readline().rstrip().decode('utf-8')
inf = float('inf') ;mod = 10**9+7
mans = inf ;ans = 0 ;count = 0 ;pro = 1

class BIT:
  # [1,n]に値が入ってる1-indexであることに注意
  def __init__(self,size):
    self.data = [0]*(size+1)
    self.size = size
  
  # [1,n]までの総和
  def sum(self,n):
    res = 0
    while n > 0:
      res += self.data[n]
      n -= n & -n
    return res
  
  def add(self,k,x):
    while k < self.size + 1:
      self.data[k] += x
      k += k & -k

n,q = map(int,input().split())
bit = BIT(n)
for _ in range(q):
  typo,x,y = map(int,input().split())
  if  typo == 0:
    bit.add(x,y)
  else:
    print(bit.sum(y)-bit.sum(x-1))