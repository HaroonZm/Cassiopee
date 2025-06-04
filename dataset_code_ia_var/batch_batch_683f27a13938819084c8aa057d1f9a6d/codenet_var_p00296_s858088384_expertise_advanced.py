from sys import stdin
from collections import deque

n, _, _ = map(int, stdin.readline().split())
a = deque(range(n))
offset = 0
for x in map(int, stdin.readline().split()):
    offset = (offset + (x if x & 1 else -x)) % n
    a.rotate(-offset)
    a.popleft()
    n -= 1
    offset %= n if n else 1

aset = set(a)
print('\n'.join(('1' if int(x) in aset else '0') for x in stdin.readline().split()))