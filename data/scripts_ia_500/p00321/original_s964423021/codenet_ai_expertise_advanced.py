from collections import Counter
from sys import stdin

n, f = map(int, stdin.readline().split())
counter = Counter(tuple(sorted(pair)) for _ in range(n)
                  for items in [stdin.readline().split()[1:]]
                  for i, a in enumerate(items) 
                  for b in items[i+1:])
results = sorted((pair for pair, count in counter.items() if count >= f))
print(len(results))
print(*zip(*results), sep='\n') if results else print(0)