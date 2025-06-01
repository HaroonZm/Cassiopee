from collections import Counter
import sys

for line in sys.stdin:
    n = int(line)
    if n == 0:
        break
    counts = Counter(int(next(sys.stdin)) for _ in range(n))
    for i in range(10):
        print('*' * counts[i] or '-')