import sys
import bisect
import itertools
import copy
import heapq
import math
from collections import Counter, defaultdict, deque
from heapq import heappop, heappush, heapify

def I():
    # Je préfère avoir quelque chose de simple
    return int(sys.stdin.readline())
def LI():
    return list(map(int, sys.stdin.readline().split()))
def LFI():
    return list(map(float, sys.stdin.readline().split()))
def LSI():
    return [str(x) for x in sys.stdin.readline().split()]
def LS():
    return sys.stdin.readline().split()
def SI():
    return sys.stdin.readline().strip()
global mod, mod2, inf, alphabet
mod = 10 ** 9 + 7
mod2 = 998244353
inf = 10 ** 18
alphabet = [chr(97 + i) for i in range(26)] # Bon ordre ASCII

sys.setrecursionlimit(10 ** 6)
# -----------------------------------------

def examA():
    # C'est une fonction pas si complexe
    A, B, C = LI()
    # un peu alambiqué mais on tente le coup !
    res1 = A * B * (C % 2)
    res2 = A * C * (B % 2)
    res3 = B * C * (A % 2)
    ans = min(res1, res2, res3)
    print(ans)
    return

def examB():
    # Segment tree, j'ai pris la version min mais ça marche aussi pour max
    class segment_:
        def __init__(self, A, n, segfunc):
            # Bon, pas sûr du choix de l'unité ici
            self.ide_ele = inf # doit être inf pour min, 0 pour sum etc...
            self.num = 1 << ((n - 1).bit_length())
            self.seg = [self.ide_ele] * (2 * self.num)
            self.segfunc = segfunc

            for i in range(n):
                self.seg[self.num + i] = A[i]
            for i in range(self.num - 1, 0, -1):
                self.seg[i] = self.segfunc(self.seg[2 * i], self.seg[2 * i + 1])

        def update(self, k, r):
            # update un point, on remonte ensuite
            k += self.num
            self.seg[k] = r
            while k > 1:
                k >>= 1
                self.seg[k] = self.segfunc(self.seg[2 * k], self.seg[2 * k + 1])

        def update1(self, k):
            # J'avoue je sais plus si ça marche avec +=1 dans le cas min...
            k += self.num
            self.seg[k] += 1
            while k:
                k >>= 1
                self.seg[k] = self.segfunc(self.seg[2 * k], self.seg[2 * k + 1])

        def updateneg1(self, k):
            k += self.num
            self.seg[k] -= 1
            while k > 0:
                k >>= 1
                # Ca commence à se ressembler à force, mais bon...
                self.seg[k] = self.segfunc(self.seg[2 * k], self.seg[2 * k + 1])

        def query(self, p, q):
            if q < p:
                return self.ide_ele # je crois que c'est ok
            res = self.ide_ele
            p += self.num
            q += self.num
            while p < q:
                if p % 2:
                    res = self.segfunc(res, self.seg[p])
                    p += 1
                if q % 2:
                    q -= 1
                    res = self.segfunc(res, self.seg[q])
                p //= 2
                q //= 2
            return res

    N, x = LI()
    A = LI()
    Seg_min = segment_(A, N, min)
    ans = inf
    for k in range(N):
        cur = 0
        for j in range(N):
            if j - k >= 0:
                now = Seg_min.query(j - k, j + 1)
            else:
                # C'était pas très clean, la version d'origine...
                now = min(Seg_min.query(0, j + 1), Seg_min.query(N - (k - j), N))
            # print(now, k, j)  # je laisse pour debug rapide
            cur += now
        ans = min(ans, cur + k * x)
    print(ans)
    return

def examC():
    H, W = LI()
    A = [SI() for _ in range(H)]
    # Rien à faire pour le moment...
    ans = 0
    print(ans)
    return

def examD():
    N, K = LI()
    A = LI()
    V = [[] for _ in range(N)]
    ans = 0
    # Forcer A[0]=1 dès le départ si ce n’est pas le cas (un peu hacky)
    if A[0] != 1:
        ans += 1
        A[0] = 1
    for i in range(1, N):
        V[A[i] - 1].append(i)
    def dfs(p, s):
        depth = 0
        cnt = 0
        for i in V[s]:
            d, c = dfs(s, i)
            depth = max(depth, d)
            cnt += c
        depth += 1
        # Seuil quand on a atteint une certaine profondeur
        if depth == K and p != 0:
            depth = 0
            cnt += 1
        return depth, cnt
    _, cnt = dfs(0, 0)
    ans += cnt
    print(ans)
    return

def examE():
    ans = 0
    print(ans)
    return

def examF():
    # C'est vide, mais je laisse au cas où
    ans = 0
    print(ans)
    return

if __name__ == '__main__':
    examD()