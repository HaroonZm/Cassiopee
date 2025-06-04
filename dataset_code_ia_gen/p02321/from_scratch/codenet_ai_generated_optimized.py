import sys
import bisect

input=sys.stdin.readline

N,W=map(int,input().split())
items=[tuple(map(int,input().split())) for _ in range(N)]

def gen_subsets(items):
    subsets = []
    n = len(items)
    for mask in range(1<<n):
        val,wt=0,0
        for i in range(n):
            if mask & (1<<i):
                v,w=items[i]
                val+=v
                wt+=w
        subsets.append((wt,val))
    return subsets

first_half = items[:N//2]
second_half = items[N//2:]

left = gen_subsets(first_half)
right = gen_subsets(second_half)

right.sort()
filtered_right = []
max_val = -1
for w,v in right:
    if filtered_right and filtered_right[-1][0]==w:
        if filtered_right[-1][1]<v:
            filtered_right[-1]=(w,v)
    else:
        filtered_right.append((w,v))

max_v = -1
clean_right = []
for w,v in filtered_right:
    if v>max_v:
        clean_right.append((w,v))
        max_v=v
right=clean_right

right_weights = [w for w,_ in right]
right_values = [v for _,v in right]

ans=0
for lw,lv in left:
    remain = W - lw
    if remain<0:
        continue
    pos = bisect.bisect_right(right_weights,remain)-1
    if pos>=0:
        ans = max(ans,lv+right_values[pos])
print(ans)