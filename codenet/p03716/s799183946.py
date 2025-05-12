#### import ####
import sys
sys.setrecursionlimit(10**7)
import math
from collections import defaultdict

#### 定数 ####
mod = 10**9 + 7

#### 読み込み ####
def I(): return int(input())
def II(): return map(int, input().split())
def III(): return list(map(int, input().split()))
def Line(N):
  read_all = [tuple(map(int, input().split())) for _ in range(N)]
  return map(list,zip(*read_all))

#################

N = I()
a = [0] + III()

from heapq import heapify,heappush,heappop
red = [0]*(3*N+1)
blue = [0]*(3*N+1)

q1 = a[1:N+1]
red[N] = sum(q1)
heapify(q1)

for k in range(N+1,2*N+1):
  heappush(q1,a[k])
  red[k] = red[k-1] + a[k] -q1[0]
  heappop(q1)

q2 = a[2*N+1:3*N+1]
blue[2*N] = sum(q2)
q2 = [(-x,x) for x in q2]
heapify(q2)

for k in range(N,2*N)[::-1]:
  heappush(q2,(-a[k+1],a[k+1]))
  blue[k] = blue[k+1] + a[k+1] -q2[0][1]
  heappop(q2)
  
ans = -float('inf')
for i in range(N,2*N+1):
  temp = red[i]-blue[i]
  if temp > ans:
    ans = temp
print(ans)