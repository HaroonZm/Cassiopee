N, F = map(int, input().split())
from collections import Counter
pairs = Counter(
    tuple(sorted((a, b)))
    for _ in range(N)
    for row in [input().split()]
    for i, a in enumerate(row[1:-1], 1)
    for b in row[i+1:]
)
ans = sorted((a, b) for (a, b), cnt in pairs.items() if cnt >= F)
print(len(ans))
if ans:
    print(*ans, sep='\n')