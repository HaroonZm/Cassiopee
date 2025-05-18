from math import sqrt
from itertools import combinations
N = int(input())

k = round((1+sqrt(1+8*N))/2)

if k*(k-1) != 2*N:
  print('No')
  exit()

print('Yes')
print(k)

S = [list() for _ in range(k)]

for i,(a,b) in enumerate(combinations(range(k),2)):
  S[a].append(i+1)
  S[b].append(i+1)

for s in S:
  print(len(s),' '.join(map(str,s)))