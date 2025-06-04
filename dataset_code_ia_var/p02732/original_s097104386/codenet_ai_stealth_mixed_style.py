N = int(input())
A = [int(x) for x in input().split()]
counter = dict()
for item in A:
    counter[item] = counter.get(item,0) + 1
from functools import reduce
def comb(k): return k*(k-1)//2 if k>1 else 0
all_vals = list(counter.values())
combo = sum([comb(k) for k in all_vals])
for idx in range(N):
    cur = A[idx]
    print(combo - (counter[cur]-1))