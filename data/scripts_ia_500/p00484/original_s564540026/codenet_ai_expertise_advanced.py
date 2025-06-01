import sys
from itertools import accumulate

def solve():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    G = [[] for _ in range(10)]
    
    for _ in range(N):
        c, g = map(int, input().split())
        G[g - 1].append(c)
    
    # Prétraitement : tri décroissant et accumulation avec bonus
    for genre in G:
        genre.sort(reverse=True)
        for i in range(1, len(genre)):
            genre[i] += genre[i-1] + 2 * i
    
    C = [0] * (K + 1)
    for genre in G:
        pre_C = C[:]
        length = len(genre)
        for n, p in zip(range(length, 0, -1), reversed(genre)):
            for i in range(K - n + 1):
                val = pre_C[i + n] + p
                if val > C[i]:
                    C[i] = val
    print(C[0])

solve()