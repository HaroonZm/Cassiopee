from sys import stdin
from itertools import islice

for line in stdin:
    try:
        num, size = map(int, line.split())
        arr = sorted(map(int, next(stdin).split()), reverse=True)
        arr[size-1::size] = [0] * ((num - size) // size + 1)
        print(sum(arr))
    except StopIteration:
        break