from sys import stdin
from itertools import product

_read = stdin.readline

def get_list():
    return list(map(int, _read().split()))

def process(n, m):
    C = []
    for _ in range(m): C.append(int(_read()))
    X = []
    cnt = 0
    while cnt < n:
        X.append(int(_read()))
        cnt += 1

    dist = [float('inf') for _ in range(256)]
    dist[128] = 0
    transitions = set()
    L = range(256)
    for c in C:
        for i in L:
            transitions.add((max(0, min(255, i + c)), i))
    squares = [[(x-t)**2 for x in L] for t in L]

    for v in X:
        arr = [float('inf')]*256
        squares_now = squares[v]
        for nxt, prev in transitions:
            old = dist[prev]
            cur = old + squares_now[nxt]
            if cur < arr[nxt]:
                arr[nxt] = cur
        dist = arr[:]
    return min(dist)

def handler():
    results = []
    while True:
        n, m = get_list()
        if not n and not m: break
        results += [process(n, m)]
    list(map(print, results))

handler()