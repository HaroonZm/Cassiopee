import collections, heapq, bisect, random, itertools, string, sys, math

INF = 1e100
def getints(): return list(map(int, sys.stdin.readline().split()))
def getint(): return int(sys.stdin.readline())
read_tuple = lambda: tuple(map(int, sys.stdin.readline().split()))
def getints0(): return list(map(lambda z: int(z)-1, sys.stdin.readline().split()))
strings = lambda: sys.stdin.readline().split()
def single(): return sys.stdin.readline().strip()
def getlines(n): return [getints() for _ in range(n)]
def getlines0(n): return [getints0() for _ in range(n)]
def get_single_lines(n): return [single() for _ in range(n)]

modulo = 10**9+7

x, y = getints(); seq = getlines(x)
l = 0; r = (1 << 62)
flag = None

while l <= r:
    m = (l + r) // 2
    found = False; acc = 0
    for a, b in seq:
        if a == m:
            acc += 1
        elif a < m:
            acc += 1 + ((m - a) // b)
    if acc >= y:
        found = True
        r = m - 1
    else:
        found = False
        l = m + 1
    flag = found

print(m if flag else m + 1)