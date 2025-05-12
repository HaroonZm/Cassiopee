import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 10**9+7
dd = [(-1,0),(0,1),(1,0),(0,-1)]
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
def pf(s): return print(s, flush=True)

class Dice():
    def __init__(self, top, front):
        # [top, front, bottom, rear, right, left]
        self.A = [top, front, 7 - top, 7 - front]
        for i in range(4):
            t = (self.A[i-1], self.A[i])
            if t == (6, 4):
                self.A += [5, 2]
            elif t == (4, 6):
                self.A += [2, 5]
            elif t == (6, 5):
                self.A += [3, 4]
            elif t == (6, 2):
                self.A += [4, 3]
            elif t == (5, 4):
                self.A += [1, 6]
            elif t == (5, 3):
                self.A += [6, 1]
            else:
                continue
            break

    def top(self):
        return self.A[0]

    def front(self):
        return self.A[1]

    def bottom(self):
        return self.A[2]

    def rear(self):
        return self.A[3]

    def right(self):
        return self.A[4]

    def left(self):
        return self.A[5]

    # di: 0 == front, 1 == rear, 2 == right, 3 == left
    def rotate(self, di):
        a = self.A
        if di == 0:
            self.A = [a[3], a[0], a[1], a[2], a[4], a[5]]
        elif di == 1:
            self.A = [a[1], a[2], a[3], a[0], a[4], a[5]]
        elif di == 2:
            self.A = [a[5], a[1], a[4], a[3], a[0], a[2]]
        elif di == 3:
            self.A = [a[4], a[1], a[5], a[3], a[2], a[0]]

def main():
    rr = []

    while True:
        n = I()
        if n == 0:
            break

        a = [LI() for _ in range(n)]
        rb = collections.defaultdict(int)
        b = collections.defaultdict(int)
        for t,f in a:
            ki = 0
            kj = 0
            d = Dice(t,f)
            f = True
            while f:
                f = False
                bt = b[(ki,kj)]
                for i in range(6,3,-1):
                    if d.front() == i and bt > b[(ki-1,kj)]:
                        f = True
                        d.rotate(0)
                        ki -= 1
                        break
                    if d.rear() == i and bt > b[(ki+1,kj)]:
                        f = True
                        d.rotate(1)
                        ki += 1
                        break
                    if d.right() == i and bt > b[(ki,kj+1)]:
                        f = True
                        d.rotate(2)
                        kj += 1
                        break
                    if d.left() == i and bt > b[(ki,kj-1)]:
                        f = True
                        d.rotate(3)
                        kj -= 1
                        break
            b[(ki,kj)] += 1
            rb[(ki,kj)] = d.top()

        r = [0] * 6
        for v in rb.values():
            if v == 0:
                continue
            r[v-1] += 1

        rr.append(' '.join(map(str,r)))

    return '\n'.join(map(str, rr))

print(main())