from collections import Counter
from sys import stdin

for line in map(str.strip, stdin):
    if (n := int(line)) == 0:
        break
    counts = Counter(int(next(stdin)) for _ in range(n))
    print('\n'.join('*' * counts.get(i, 0) or '-' for i in range(10)))