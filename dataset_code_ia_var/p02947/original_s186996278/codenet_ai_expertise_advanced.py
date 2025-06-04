from collections import Counter, defaultdict
from sys import stdin

N = int(stdin.readline())
strings = [stdin.readline().strip() for _ in range(N)]

count = Counter(''.join(sorted(s)) for s in strings)

ans = sum(v * (v - 1) // 2 for v in count.values())

print(ans)