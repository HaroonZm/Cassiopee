from collections import Counter
N, F = map(int, input().split())
pair_count = Counter()
for _ in range(N):
    items = input().split()[1:]
    items.sort()
    for i in range(len(items)):
        for j in range(i+1, len(items)):
            pair_count[(items[i], items[j])] += 1
res = [pair for pair, cnt in pair_count.items() if cnt >= F]
res.sort()
print(len(res))
for a, b in res:
    print(a, b)