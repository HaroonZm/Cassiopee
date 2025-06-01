import sys
sys.setrecursionlimit(10**7)
W,H = map(int,input().split())
Grid = [list(map(int,input().split())) for _ in range(H)]
SumW = [[0 for _ in range(W)] for __ in range(H)]
SumH = [[0 for _ in range(W)] for __ in range(H)]
for r in range(H):
    accumulator = 0
    c = W-1
    while c >= 0:
        accumulator += Grid[r][c]
        SumW[r][c] = accumulator
        c -= 1
for c in range(W):
    accumulator = 0
    r = H-1
    while r >= 0:
        accumulator += Grid[r][c]
        SumH[r][c] = accumulator
        r -= 1

cache = {}

def traverse(x:int,y:int)->int:
    if (x,y) in cache:
        return cache[(x,y)]
    if x == W or y == H:
        return 0
    if (x+y) & 1 == 0:
        # player one tries to maximize outcome
        res = max(traverse(x+1,y) - SumH[y][x], traverse(x,y+1) + SumW[y][x])
    else:
        # player two tries to minimize outcome
        res = min(traverse(x+1,y) - SumH[y][x], traverse(x,y+1) + SumW[y][x])
    cache[(x,y)] = res
    return res

print(abs(traverse(0,0)))