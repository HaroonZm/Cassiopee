from sys import exit, setrecursionlimit, stderr
from functools import reduce
from itertools import *
from collections import *
from bisect import *
from heapq import *

def read():
  return int(input())
 
def reads():
  return [int(x) for x in input().split()]

N = read()
A = reads()

c1 = sum(a % 2 == 1 for a in A)
c2 = sum(a % 4 == 2 for a in A)
c4 = sum(a % 4 == 0 for a in A)

if c1 > c4 + 1 or (c1 == c4 + 1 and c2 > 0):
  print("No")
else:
  print("Yes")