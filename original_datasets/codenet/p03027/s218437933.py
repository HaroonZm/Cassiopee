from sys import exit, setrecursionlimit, stderr, stdin
from functools import reduce
from itertools import *
from collections import defaultdict, Counter
from bisect import bisect
import functools

setrecursionlimit(10**7)

def input():
  return stdin.readline().strip()

def read():
  return int(input())

def reads():
  return [int(x) for x in input().split()]

MOD = 10**6 + 3

fact = [1] * MOD
for i in range(1, MOD):
  fact[i] = (fact[i-1] * i) % MOD
invfact = [0] * MOD; invfact[-1] = pow(fact[-1], MOD-2, MOD)
for i in range(MOD-2, -1, -1):
  invfact[i] = invfact[i+1] * (i+1) % MOD
# print(invfact[:10])

def inv(n):
  return pow(n, MOD-2, MOD)

def solve(x, d, n):
  if x == 0:
    return 0
  if d == 0:
    return pow(x, n, MOD)
  k = x * inv(d) % MOD
  if n + k - 1 >= MOD:
    return 0
  return fact[n + k - 1] * invfact[k-1] % MOD * pow(d, n, MOD) % MOD

Q = read()
for _ in range(Q):
  x, d, n = reads()
  ans = solve(x, d, n)
  print(ans)