import sys
import bisect
input=sys.stdin.readline

N,M=map(int,input().split())
pictures=[tuple(map(int,input().split())) for _ in range(N)]
frames=[int(input()) for _ in range(M)]

pictures.sort(key=lambda x:(x[1],x[0]))
frames.sort()

res=0
from collections import Counter
frame_count=Counter(frames)
sizes=sorted(frame_count)

import heapq

heap=[]
idx=0
for v,s in pictures:
    while idx<len(sizes) and sizes[idx]<=s:
        for _ in range(frame_count[sizes[idx]]):
            heapq.heappush(heap,sizes[idx])
        idx+=1
    pos=bisect.bisect_left(heap,s)
    if pos==len(heap):
        continue
    # remove one frame >= s
    # but can't remove from heap by index, so pop min until >= s
    # so we use a loop
    tmp=[]
    found=False
    while heap:
        f=heapq.heappop(heap)
        if not found and f>=s:
            found=True
            res+=1
            break
        else:
            tmp.append(f)
    for x in tmp:
        heapq.heappush(heap,x)

print(res)