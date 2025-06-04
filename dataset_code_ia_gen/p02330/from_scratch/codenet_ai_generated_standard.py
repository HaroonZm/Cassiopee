from sys import stdin
from bisect import bisect_left, bisect_right
from collections import defaultdict

def comb_sums(arr, K):
    n = len(arr)
    res = defaultdict(list)
    def dfs(i, k, s):
        if k > K:
            return
        if i == n:
            res[k].append(s)
            return
        dfs(i+1, k, s)
        dfs(i+1, k+1, s+arr[i])
    dfs(0,0,0)
    return res

N,K,L,R = map(int, stdin.readline().split())
a = list(map(int, stdin.readline().split()))

half = N//2
left = a[:half]
right = a[half:]

left_sums = comb_sums(left,K)
right_sums = comb_sums(right,K)

for k in left_sums:
    right_sums.setdefault(K - k, [])

for v in right_sums.values():
    v.sort()

count = 0
for k_left, sums_left in left_sums.items():
    k_right = K - k_left
    if k_right < 0 or k_right not in right_sums:
        continue
    sums_right = right_sums[k_right]
    for s_left in sums_left:
        low = L - s_left
        high = R - s_left
        l_idx = bisect_left(sums_right, low)
        r_idx = bisect_right(sums_right, high)
        count += r_idx - l_idx

print(count)