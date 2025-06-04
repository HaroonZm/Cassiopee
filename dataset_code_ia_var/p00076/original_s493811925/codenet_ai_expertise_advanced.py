import sys
from itertools import islice, count

def walk(n):
    z = 1
    yield z
    for _ in range(1, n):
        z += (d := z * 1j) / abs(d)
        yield z

for line in map(str.strip, sys.stdin):
    if line == '-1':
        break
    n = int(line)
    *_, z = islice(walk(n), n)
    print(f"{z.real}\n{z.imag}")