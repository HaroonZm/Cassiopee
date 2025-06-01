from collections import Counter

n, f = map(int, input().split())
counter = Counter()

for _ in range(n):
    m, *c = input().split()
    pairs = ((min(c[i], c[j]), max(c[i], c[j])) for i in range(int(m) - 1) for j in range(i + 1, int(m)))
    counter.update(pairs)

filtered_pairs = [pair for pair, count in counter.items() if count >= f]
filtered_pairs.sort()
print(len(filtered_pairs))
for pair in filtered_pairs:
    print(*pair)