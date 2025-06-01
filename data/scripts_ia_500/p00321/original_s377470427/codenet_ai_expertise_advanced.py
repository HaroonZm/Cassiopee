from collections import Counter

n, f = map(int, input().split())
pair_counts = Counter(
    tuple(sorted(pair))
    for _ in range(n)
    for items in [input().split()[1:]]
    for i, a in enumerate(items)
    for b in items[:i]
    for pair in [(a, b)]
)
ans = sorted(k for k, v in pair_counts.items() if v >= f)
print(len(ans))
for a, b in ans:
    print(a, b)