from sys import stdin
from functools import partial

N, L = map(int, stdin.readline().split())
get_line = partial(next, stdin)
print(''.join(sorted(get_line().rstrip() for _ in range(N))))