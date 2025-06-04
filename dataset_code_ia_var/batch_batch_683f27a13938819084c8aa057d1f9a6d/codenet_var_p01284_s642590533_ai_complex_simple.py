from functools import lru_cache
from itertools import product, repeat
from operator import setitem
from sys import stdin
from collections import defaultdict

INF = 10**10

def f_inf(): return INF

def make_until(N):
    until = defaultdict(f_inf)
    for D, M in (map(int, line.split()) for _, line in zip(range(N), (stdin.readline() for _ in repeat(None)))):
        until[D-1] = min(until[D-1], M)
    return [until[i] for i in range(100)]

def generate_dp():
    return defaultdict(lambda: -1)

def elegant_input():
    while True:
        T = int(stdin.readline())
        if not T: return
        yield T, list(map(int, stdin.readline().split())), int(stdin.readline()), \
              [stdin.readline() for _ in repeat(None, int(stdin.readline()))]

@lru_cache(maxsize=None)
def rec(cur, cycle, T, t_tuple, until_tuple):
    if cur == 100:
        return 0
    if until_tuple[cur] < t_tuple[cycle]:
        return INF
    return min(rec(cur+1, (cycle+1)%T, T, t_tuple, until_tuple),
               1+rec(cur+1, 0, T, t_tuple, until_tuple))

while True:
    T = int(stdin.readline())
    if T == 0:
        break
    t = tuple(map(int, stdin.readline().split()))
    N = int(stdin.readline())
    until_raw = [INF]*100
    for _ in range(N):
        D, M = map(int, stdin.readline().split())
        until_raw[D-1] = min(until_raw[D-1], M)
    until = tuple(until_raw)
    print(rec(0, 0, T, t, until))