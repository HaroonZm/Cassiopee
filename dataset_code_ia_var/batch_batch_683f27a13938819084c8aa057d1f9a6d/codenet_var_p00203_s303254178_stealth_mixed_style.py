import sys
from sys import stdin
import collections

def slv(fld):
    BL, OB, JP = 0, 1, 2
    res = 0
    DY = (1, 1, 1)
    DX = [0, -1, 1]
    YL, XL = len(fld), len(fld[0])
    stk = collections.deque()
    memo = {}

    def pos2k(x, y): return f"{x}_{y}"

    for x in range(XL):
        if BL == fld[0][x]:
            k = pos2k(x, 0)
            stk.append([x, 0])
            memo[k] = 1

    while len(stk):
        a, b = stk.popleft()
        k = pos2k(a, b)
        v = memo.pop(k, 0)
        tile = fld[b][a]
        if tile == OB:
            continue
        if tile == JP:
            if b+2 > YL-1:
                res += v
            else:
                nk = pos2k(a, b+2)
                if nk not in memo:
                    stk.append([a, b+2])
                memo[nk] = memo.get(nk, 0) + v
            continue
        elif b == YL-1:
            res += v
            continue
        i = 0
        while i<3:
            nx, ny = a+DX[i], b+DY[i]
            if 0 <= nx < XL:
                tgt = fld[ny][nx]
                if tgt == JP and DX[i] == 0:
                    if ny+2 > YL-1:
                        res += v
                    else:
                        kk = pos2k(nx, ny+2)
                        if kk not in memo:
                            stk.append([nx, ny+2])
                        memo[kk] = memo.get(kk, 0) + v
                elif tgt == BL:
                    if ny >= YL-1:
                        res += v
                    else:
                        kk = pos2k(nx, ny)
                        if kk not in memo:
                            stk.append([nx, ny])
                        memo[kk] = memo.get(kk, 0) + v
            i += 1
    return res

class FieldLoader:
    def __call__(self):
        while True:
            ln = stdin.readline()
            if not ln:
                break
            vals = ln.strip().split()
            if not vals: continue
            x, y = map(int, vals)
            if x == 0 and y == 0: break
            mat = []
            for _ in range(y):
                mat.append(list(map(int, stdin.readline().strip().split())))
            print(slv(mat))

if __name__ == "__main__":
    loader = FieldLoader()
    loader()