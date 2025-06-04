from collections import Counter

N = int(input())
V = list(map(int, input().split()))

v1 = Counter(V[::2])
v2 = Counter(V[1::2])

top_v1 = v1.most_common(2) + [(None, 0)]
top_v2 = v2.most_common(2) + [(None, 0)]

min_changes = float('inf')
for (val1, cnt1) in top_v1[:2]:
    for (val2, cnt2) in top_v2[:2]:
        if val1 != val2:
            changes = N - cnt1 - cnt2
            if changes < min_changes:
                min_changes = changes

if min_changes == float('inf'):
    min_changes = N // 2

print(min_changes)