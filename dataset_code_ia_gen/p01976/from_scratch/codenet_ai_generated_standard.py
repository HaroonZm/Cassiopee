import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())
a = list(map(int, input().split()))

prefix_count = Counter()
suffix_count = Counter(a[N-1:])
res = []

for i in range(N):
    prefix_count[a[i]] += 1
    suffix_count[a[N - i - 1]] -= 1
    if suffix_count[a[N - i - 1]] == 0:
        del suffix_count[a[N - i - 1]]
    if prefix_count == suffix_count:
        res.append(i + 1)

print(*res)