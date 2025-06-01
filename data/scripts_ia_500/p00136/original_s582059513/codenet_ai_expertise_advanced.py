from collections import Counter
from sys import stdin

C = Counter()
for _ in range(int(stdin.readline())):
    a, _ = map(int, stdin.readline().split('.'))
    idx = 0 if a < 165 else (a - 160) // 5
    C[idx] += 1
for i in range(6):
    print(f"{i+1}:{'*' * C[i]}")