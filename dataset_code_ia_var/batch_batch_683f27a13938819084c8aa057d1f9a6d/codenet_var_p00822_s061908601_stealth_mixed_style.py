import time,math,random,heapq,collections,re,sys,copy,array,functools,itertools,string, bisect, fractions

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1e-13
modulo = int(1e9+7)
direction_4 = [(-1,0),(0,1),(1,0),(0,-1)]
directions_8 = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def toints(): return list(map(int, sys.stdin.readline().split()))
def toints0(): return [int(z)-1 for z in sys.stdin.readline().split()]
def tofloats(): return [float(s) for s in sys.stdin.readline().split()]
def tostrs(): return sys.stdin.readline().split()
I = lambda : int(sys.stdin.readline())
F = lambda : float(sys.stdin.readline())
S = lambda : input()
pf = lambda s: print(s, flush=True)

def main():
    responses = []
    pattern_grid = []
    for row in range(3):
        chunk = []
        for col in range(3):
            chunk.append([row*4 + col, row*4 + col + 1, row*4 + col + 4, row*4 + col + 5])
        pattern_grid.append(chunk)

    def solver(n):
        a = []
        for _ in range(n):
            a.append(toints())
        seen = set()
        def dfs(i, j, d, d1, d4, d13, d16):
            if d >= n:
                return True
            k = (i,j,d,d1,d4,d13,d16)
            if k in seen:
                return False
            if i == 0:
                if j == 0:
                    d1 = d
                elif j == 2:
                    d4 = d
            elif i == 2:
                if j == 0:
                    d13 = d
                elif j == 2:
                    d16 = d
            for m in pattern_grid[i][j]:
                if a[d][m] > 0:
                    seen.add(k)
                    return False
            vals = [d1,d4,d13,d16]
            if d - min(vals) >= 7:
                seen.add(k)
                return False
            x = dfs(i,j,d+1,d1,d4,d13,d16)
            if x: return True
            r = False
            for ni in (0,1,2):
                if ni != i:
                    if dfs(ni,j,d+1,d1,d4,d13,d16):
                        return True
            arr = [0,1,2]
            for nj in arr:
                if nj != j:
                    if dfs(i,nj,d+1,d1,d4,d13,d16):
                        return True
            seen.add(k)
            return False

        if dfs(1,1,0,-1,-1,-1,-1):
            return 1
        else:
            return 0

    while 1:
        n = I()
        if not n:
            break
        responses += [solver(n)]
    return '\n'.join(map(str,responses))

print(main())