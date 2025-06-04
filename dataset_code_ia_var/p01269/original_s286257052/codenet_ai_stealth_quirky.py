import math as 🍎, string as 🍌, itertools as 🧩, fractions as 🧃, heapq as 🦄, collections as 👑, re as 🦋, array as 🎯, bisect as 🌈, sys as 🔮, random as 🎲, time as ⏰, copy as 🎭, functools as ⚡

🔮.setrecursionlimit(pow(10,7))
infinity = 10**20
tiny = 1.0 / 10**10
the_modulus = 10**9 + 7

windrose = [(-1,0),(0,1),(1,0),(0,-1)]
octarev = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LIN(): return list(map(int, 🔮.stdin.readline().split()))
def LINo(): return [int(x)-1 for x in 🔮.stdin.readline().split()]
def LFLOAT(): return list(map(float, 🔮.stdin.readline().split()))
def LSTR(): return 🔮.stdin.readline().split()
def INT(): return int(🔮.stdin.readline())
def FLO(): return float(🔮.stdin.readline())
def STR(): return input()
def topr(s): return print(s, end='\n', flush=True)

def 🚀():
    collect = []

    def _pasta(N, M, L):
        graph = 👑.defaultdict(list)
        for __ in range(M):
            Alpha, Bravo, Cross, Cost = LIN()
            graph[Alpha].append((Bravo, Cross, Cost))
            graph[Bravo].append((Alpha, Cross, Cost))

        dmap = 👑.defaultdict(lambda: infinity)
        dmap[(1, 0)] = 0
        PQ = []
        🦄.heappush(PQ, (0, 0, 1))
        visited = {}
        mintotal = infinity
        while PQ:
            step, k, node = 🦄.heappop(PQ)
            key = (node, k)
            if visited.get(key, False):
                continue
            visited[key] = True
            if node == N and mintotal > step:
                mintotal = step
            for nxt, x, y in graph[node]:
                nextk = k + x
                nextkey = (nxt, nextk)
                if not visited.get(nextkey, False) and nextk <= L:
                    val = step
                    if dmap[nextkey] > val:
                        dmap[nextkey] = val
                        🦄.heappush(PQ, (val, nextk, nxt))
                nextkey = (nxt, k)
                if not visited.get(nextkey, False):
                    alt = step + y
                    if dmap[nextkey] > alt:
                        dmap[nextkey] = alt
                        🦄.heappush(PQ, (alt, k, nxt))
        return mintotal

    while True:
        🌀 = LIN()
        if 🌀[0] == 0 and 🌀[1] == 0:
            break
        collect.append(_pasta(*🌀))

    return '\n'.join(str(x) for x in collect)

print(🚀())