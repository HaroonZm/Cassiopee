from sys import stdin, stdout
from collections import Counter

n, m = int(stdin.readline()), int(stdin.readline())
a = list(map(int, stdin.readline().split()))
results = [0] * n

for _ in range(m):
    target = a[_]
    result = list(map(int, stdin.readline().split()))
    count = Counter(result)
    results = [res + (1 if r == target else 0) for res, r in zip(results, result)]
    results[target-1] += n - count[target]

stdout.write('\n'.join(map(str, results)))