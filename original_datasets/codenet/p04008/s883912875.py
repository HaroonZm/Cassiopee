def examA():
    A, B, C = LI()
    ans = min(A*B*(C%2),A*C*(B%2),B*C*(A%2))
    print(ans)
    return

def examB():
    class segment_():
        def __init__(self, A, n, segfunc):
            #####単位元######要設定0or1orinf
            self.ide_ele = inf
            ####################
            self.num = 1 << (n - 1).bit_length()
            self.seg = [self.ide_ele] * 2 * self.num
            self.segfunc = segfunc
            # set_val
            for i in range(n):
                self.seg[i + self.num] = A[i]
                # built
            for i in range(self.num - 1, 0, -1):
                self.seg[i] = self.segfunc(self.seg[2 * i], self.seg[2 * i + 1])

        def update(self, k, r):
            k += self.num
            self.seg[k] = r
            while k:
                k >>= 1
                self.seg[k] = self.segfunc(self.seg[k * 2], self.seg[k * 2 + 1])

        # 値xに1加算
        def update1(self, k):
            k += self.num
            self.seg[k] += 1
            while k:
                k >>= 1
                self.seg[k] = self.segfunc(self.seg[k * 2], self.seg[k * 2 + 1])

        def updateneg1(self, k):
            k += self.num
            self.seg[k] -= 1
            while k:
                k >>= 1
                self.seg[k] = self.segfunc(self.seg[k * 2], self.seg[k * 2 + 1])

        def query(self, p, q):
            if q < p:
                return self.ide_ele
            p += self.num;
            q += self.num
            res = self.ide_ele
            while p < q:
                if p & 1 == 1:
                    res = self.segfunc(res, self.seg[p])
                    p += 1
                if q & 1 == 1:
                    q -= 1
                    res = self.segfunc(res, self.seg[q])
                p >>= 1;
                q >>= 1
            return res
    N, x = LI()
    A = LI()
    Seg_min = segment_(A, N, lambda a, b: min(a,b))
    ans = inf
    for k in range(N):
        cur = 0
        for j in range(N):
            if j-k>=0:
                now = Seg_min.query(j-k,j+1)
            else:
                now = min(Seg_min.query(0,j+1),Seg_min.query(N-(k-j),N))
#            print(now,k,j)
            cur += now
        ans = min(ans,cur+k*x)

    print(ans)
    return

def examC():
    H, W = LI()
    A = [SI()for _ in range(H)]

    ans = 0
    print(ans)
    return

def examD():
    N, K = LI()
    A = LI()
    V = [[]for _ in range(N)]
    ans = 0
    if A[0]!=1:
        ans += 1
        A[0] = 1
    for i in range(1,N):
        V[A[i]-1].append(i)
    def dfs(p,s):
        depth = 0
        cnt = 0
        for i in V[s]:
            d,c = dfs(s,i)
            depth = max(depth,d)
            cnt += c
        depth += 1
        if depth==K and p!=0:
            depth = 0
            cnt += 1
        return depth,cnt
    _,cnt = dfs(0,0)
    ans += cnt
    print(ans)
    return

def examE():
    ans = 0
    print(ans)
    return

def examF():
    ans = 0
    print(ans)
    return

import sys,copy,bisect,itertools,heapq,math
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LFI(): return list(map(float,sys.stdin.readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
global mod,mod2,inf,alphabet
mod = 10**9 + 7
mod2 = 998244353
inf = 10**18
alphabet = [chr(ord('a') + i) for i in range(26)]

sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    examD()

"""

"""