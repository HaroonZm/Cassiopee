N,R,T=map(int,input().split())
paces=[int(input()) for _ in range(N)]
from collections import defaultdict
count=defaultdict(int)
for p in paces:
    for t in range(T+1):
        pos = (p*t)%R
        count[(pos,t%2)] += 1
print(max(count.values()))