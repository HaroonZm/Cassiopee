from sys import stdin
from itertools import count

n = int(stdin.readline())
m = set()

for _ in range(n):
    a, b = map(int, stdin.readline().split())
    for i in count():
        val = a + b + i
        if val in m:
            m.remove(val)
        else:
            m.add(val)
            break

for val in sorted(m):
    print(f"{val} 0")