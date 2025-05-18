from sys import setrecursionlimit
setrecursionlimit(100000)

class Cake():

    def __init__(self, N, W, D):
        self.P = [-1]*2*(N+1)
        self.L = [-1]*2*(N+1)
        self.R = [-1]*2*(N+1)
        self.W = [0]*2*(N+1)
        self.W[1] = W
        self.D = [0]*2*(N+1)
        self.D[1] = D

    def find(self, target):
        count = 0
        for i in range(1, 2*N+2):
            count += (self.L[i] == -1)
            if count == target:
                return i

    def cut(self, target, s, l):
        w = self.W[target]
        d = self.D[target]
        L = w+d
        s %= L
        if s <= w:
            nw, nW = s, w-s
            if nw > nW:
                nw, nW = nW, nw
            nd, nD = d, d
        else:
            s -= w
            nd, nD = s, d-s
            if nd > nD:
                nd, nD = nD, nd
            nw, nW = w, w
        assert 0 < nw
        assert 0 < nd
        r = l + 1
        self.L[target], self.R[target] = l, r
        self.P[l], self.P[r] = target, target
        self.W[l], self.W[r] = nw, nW
        self.D[l], self.D[r] = nd, nD

    def show(self):
        tmp = []
        for i in range(1, len(self.L)):
            if self.L[i] == -1:
                tmp.append(self.W[i] * self.D[i] )
        print(" ".join(map(str, sorted(tmp))))

N, W, D = map(int, input().split())
while W:
    cake = Cake(N, W, D)
    for i in range(N):
        p, s = map(int, input().split())
        target = cake.find(p)
        cake.cut(target, s, 2*(i+1))
    cake.show()
    N, W, D = map(int, input().split())