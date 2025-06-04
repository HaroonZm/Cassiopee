from itertools import count
from sys import exit

def func(n: int) -> int:
    return n // 2 if n & 1 == 0 else 3 * n + 1

s = int(input())
seen = {s}
val = s
for i in count(1):
    val = func(val)
    if val in seen:
        print(i + 1)
        exit()
    seen.add(val)