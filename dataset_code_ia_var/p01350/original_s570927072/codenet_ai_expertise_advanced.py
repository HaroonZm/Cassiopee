import sys
import math
import collections
from typing import List

# Optimisation : alias pour accès rapide
readline = sys.stdin.readline

sys.setrecursionlimit(10**7)

INF = float('inf')
EPS = 1.0e-13
MOD = 10**9 + 7
DIR4 = [(-1,0), (0,1), (1,0), (0,-1)]
DIR8 = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]

def LI() -> List[int]:
    return list(map(int, readline().split()))

def LI_() -> List[int]:
    return [x - 1 for x in map(int, readline().split())]

def LF() -> List[float]:
    return list(map(float, readline().split()))

def LS() -> List[str]:
    return readline().split()

def I() -> int:
    return int(readline())

def F() -> float:
    return float(readline())

def S() -> str:
    return input()

def pf(s):
    print(s, flush=True)

def main():
    results = []

    def solve():
        n = I()
        r, t = LF()
        points = [LI() for _ in range(n)]

        # Matrices optimisées avec list comprehensions et dict comprehensions
        angle = {(i, j): math.degrees(math.atan2(points[j][0] - points[i][0], points[j][1] - points[i][1]))
                 for i in range(n) for j in range(n) if i != j}
        dist = {(i, j): math.hypot(points[i][0] - points[j][0], points[i][1] - points[j][1])
                for i in range(n) for j in range(n)}
        
        # Pré-calcul des transitions valides
        edges = collections.defaultdict(list)
        for i in range(n):
            for j in range(n):
                if i == j: continue
                dij = angle.get((i, j), None)
                if dij is None:
                    continue
                for k in range(n):
                    if k == j: continue
                    djk = angle.get((j, k), None)
                    if djk is None:
                        continue
                    diff = abs(dij - djk)
                    if diff <= t or 360 - diff <= t:
                        edges[(i, j)].append(((j, k), dist[(j, k)]))

        # Recherche dynamique avancée
        dp = [[None] * n for _ in range(n)]
        best = 0
        for j in range(1, n):
            if (cost := dist[(0, j)]) <= r:
                dp[0][j] = cost
                best = 1

        if not best:
            return 0

        while True:
            updated = False
            ndp = [[None] * n for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    v = dp[i][j]
                    if v is None:
                        continue
                    for (jnext, knext), add_cost in edges.get((i, j), ()):
                        total = v + add_cost
                        if total > r:
                            continue
                        prev = ndp[j][knext]
                        if prev is None or total < prev:
                            ndp[j][knext] = total
                            updated = True
            if not updated:
                break
            dp = ndp
            best += 1
        return best

    # Boucle d'un seul cas
    results.append(solve())
    return '\n'.join(map(str, results))

print(main())