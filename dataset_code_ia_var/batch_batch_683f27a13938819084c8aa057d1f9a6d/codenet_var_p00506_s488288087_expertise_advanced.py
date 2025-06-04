from itertools import count, compress
from sys import stdin

n = int(stdin.readline())
values = list(map(int, stdin.readline().split()))
minv = min(values) + 1

print(1)

is_ok = bytearray([1]) * minv
for i in count(2):
    if i >= minv:
        break
    if all(v % i != 0 for v in values):
        print(i)
    else:
        is_ok[i:minv:i] = b'\x00' * ((minv-1)//i)
    try:
        i = next(j for j in range(i+1, minv) if is_ok[j])
    except StopIteration:
        break