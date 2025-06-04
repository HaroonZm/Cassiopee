from functools import reduce
from itertools import groupby, count, accumulate, chain

s = input()
n = len(s)

ans = [0]*n

def reflect(i, j): return i + ((abs(j-i)) % 2)

pairs = [(i, i+1) for i in range(n-1) if s[i:i+2] == "RL"]

for i, _ in pairs:
    # Process consecutive R's to the left of i
    left = (next(g) for k, g in groupby((j for j in range(i, -1, -1)), lambda x: s[x]=='R') if k)
    for idx in next(left, []):
        ans[reflect(i, idx)] += 1
    # Process consecutive L's to the right of i+1
    right = (next(g) for k, g in groupby((j for j in range(i+1, n)), lambda x: s[x]=='L') if k)
    for idx in next(right, []):
        ans[reflect(i, idx)] += 1

print(*map(str, ans))