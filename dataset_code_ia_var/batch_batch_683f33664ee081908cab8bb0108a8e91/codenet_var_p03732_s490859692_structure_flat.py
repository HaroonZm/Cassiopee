N_W = input().split()
N = int(N_W[0])
W = int(N_W[1])
Items = []
i = 0
while i < N:
    line = input().split()
    Items.append((int(line[0]), int(line[1])))
    i += 1
from collections import defaultdict as dd
Bag = dd(lambda:0)
Bag[0] = 0
idx = 0
while idx < len(Items):
    w = Items[idx][0]
    v = Items[idx][1]
    keys = list(Bag.keys())
    temp = []
    j = 0
    while j < len(keys):
        key = keys[j]
        if key + w <= W:
            temp.append((key + w, Bag[key] + v))
        j += 1
    k = 0
    while k < len(temp):
        key, value = temp[k]
        Bag[key] = max(Bag[key], value)
        k += 1
    idx += 1
vals = list(Bag.values())
ans = vals[0]
p = 1
while p < len(vals):
    if vals[p] > ans:
        ans = vals[p]
    p += 1
print(ans)