import sys, random
from collections import Counter
from heapq import *
import math as m

def R(): return int(sys.stdin.readline())
def RL(): return list(map(int, sys.stdin.readline().split()))
def RLN(x): return [int(sys.stdin.readline()) for _ in range(x)]

get = lambda: input()
res = 1

s = get()
length = len(s) if s else 0
mycnt = Counter(s)
X = 0
keys = list(mycnt)
i = 0
while i < len(keys):
    k = keys[i]
    v = mycnt[k]
    if v > 1:
        X += v*(v-1)//2
    i += 1
total = (length*(length-1))//2
print((total - X) + res)