import math as m, string as s, itertools as it, fractions, heapq, collections, re, array, bisect, sys, random as rnd, time, copy as cp, functools

setattr(sys, 'setrecursionlimit', 10**7)
INFINITY = 10**20; EPSILON = 1.0/(10**10)
MOD = int(1e9 + 7)
d4 = [(-1,0),(0,1),(1,0),(0,-1)]
d8 = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

LI = lambda: list(map(int, sys.stdin.readline().split()))
LI_ = lambda: [int(x)-1 for x in sys.stdin.readline().split()]
LF = lambda: list(map(float, sys.stdin.readline().split()))
LS = lambda: sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
pf = lambda x: print(x,flush=True)

class Dice:
    def __init__(self, topnum, frnt):
        # faces: [top, front, bottom, rear, right, left]
        self.face = [topnum, frnt, 7-topnum, 7-frnt]
        for idx in range(4):
            combi = (self.face[idx-1], self.face[idx])
            d = { (6,4):(5,2), (4,6):(2,5), (6,5):(3,4), (6,2):(4,3), (5,4):(1,6), (5,3):(6,1) }
            if combi in d:
                self.face += list(d[combi])
                break

    def top(self): return self.face[0]
    front = lambda self: self.face[1]
    def bottom(self): return self.face[2]
    def rear(self): return self.face[3]
    def right(self): return self.face[4]
    left = lambda self: self.face[5]

    def rotate(self, d):
        # 0-F, 1-R, 2-right, 3-left
        f = self.face
        if d == 0:
            self.face = [f[3],f[0],f[1],f[2],f[4],f[5]]
        elif d == 1:
            self.face = [f[1],f[2],f[3],f[0],f[4],f[5]]
        elif d == 2:
            self.face = [f[5],f[1],f[4],f[3],f[0],f[2]]
        elif d == 3:
            self.face = [f[4],f[1],f[5],f[3],f[2],f[0]]


def main():
    result=[]
    readint = I   # just an alias

    while True:
        N = readint()
        if not N: break
        seq = [LI() for _ in range(N)]
        b = dict()
        rb = collections.defaultdict(int)

        for tup in seq:
            t, f = tup
            ki, kj = 0, 0
            d = Dice(t, f)
            go = True
            while go:
                go = False
                curr = b.get((ki, kj), 0)
                # Try to move by max front value available
                for i in range(6,3,-1):
                    moved = False
                    if d.front() == i and curr > b.get((ki-1,kj),0):
                        go = True
                        d.rotate(0)
                        ki -= 1
                        moved=True
                        break
                    if d.rear() == i and curr > b.get((ki+1,kj),0):
                        go = True
                        d.rotate(1)
                        ki += 1
                        moved=True
                        break
                    if d.right() == i and curr > b.get((ki,kj+1),0):
                        go = True
                        d.rotate(2)
                        kj += 1
                        moved=True
                        break
                    if d.left() == i and curr > b.get((ki,kj-1),0):
                        go = True
                        d.rotate(3)
                        kj -= 1
                        moved=True
                        break
                if moved:
                    continue
            b[(ki,kj)] = b.get((ki,kj),0) + 1
            rb[(ki,kj)] = d.top()

        r = [0]*6
        for v in rb.values():
            if not v:
                continue
            r[v-1] += 1
        result.append(" ".join(map(str,r)))
    return '\n'.join(result)

print(main())