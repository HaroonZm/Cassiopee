from sys import exit, setrecursionlimit, stderr
from functools import reduce
from itertools import *
from collections import defaultdict
from bisect import bisect
from random import *

def read():
  return int(input())
 
def reads():
  return [int(x) for x in input().split()]
 
N = read()
A = reads()

print(2 * N)
m = min(A)
M = max(A)
if abs(m) <= abs(M):
  I = A.index(M) + 1
  print(I, 1)
  print(I, 1)
  for i in range(1, N):
    print(i, i+1)
    print(i, i+1)
else:
  I = A.index(m) + 1
  print(I, N)
  print(I, N)
  for i in range(N, 1, -1):
    print(i, i-1)
    print(i, i-1)