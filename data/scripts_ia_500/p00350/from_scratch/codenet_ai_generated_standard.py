import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

MOD1 = 10**9 + 7
MOD2 = 10**9 + 9
BASE = 131

class SegmentTree:
    def __init__(self, s):
        self.n = len(s)
        self.size = 1
        while self.size < self.n:
            self.size <<= 1
        self.hash1 = [0]*(self.size<<1)
        self.hash2 = [0]*(self.size<<1)
        self.lazy = [None]*(self.size<<1)
        self.pow1 = [1]*(self.n+1)
        self.pow2 = [1]*(self.n+1)
        for i in range(self.n):
            self.hash1[self.size+i] = ord(s[i]) - ord('a') + 1
            self.hash2[self.size+i] = ord(s[i]) - ord('a') + 1
        for i in range(self.n):
            self.pow1[i+1] = self.pow1[i]*BASE % MOD1
            self.pow2[i+1] = self.pow2[i]*BASE % MOD2
        for i in range(self.size-1, 0, -1):
            self._update(i)

    def _update(self, i):
        self.hash1[i] = (self.hash1[i<<1]*self.pow1[self._len(i<<1|1)] + self.hash1[i<<1|1]) % MOD1
        self.hash2[i] = (self.hash2[i<<1]*self.pow2[self._len(i<<1|1)] + self.hash2[i<<1|1]) % MOD2

    def _len(self, i):
        l = 1
        while i < self.size:
            i <<= 1
            l <<= 1
        return l

    def _apply(self, i, c):
        length = self._len(i)
        val = ord(c) - ord('a') + 1
        self.hash1[i] = (val * (self.pow1[length]-1) * pow(BASE-1, MOD1-2, MOD1)) % MOD1
        self.hash2[i] = (val * (self.pow2[length]-1) * pow(BASE-1, MOD2-2, MOD2)) % MOD2
        self.lazy[i] = c

    def _push(self, i):
        if self.lazy[i] is not None:
            self._apply(i<<1, self.lazy[i])
            self._apply(i<<1|1, self.lazy[i])
            self.lazy[i] = None

    def _push_to(self, i):
        h = i.bit_length()
        for s in range(h-1, 0, -1):
            j = i>>s
            if self.lazy[j] is not None:
                self._push(j)

    def update(self, l, r, c):
        l += self.size - 1
        r += self.size - 1
        l0, r0 = l, r
        while l <= r:
            if l & 1 == 1:
                self._apply(l, c)
                l += 1
            if r & 1 == 0:
                self._apply(r, c)
                r -= 1
            l >>= 1
            r >>= 1
        for i in {l0, r0}:
            while i > 1:
                i >>= 1
                if self.lazy[i] is None:
                    self._update(i)

    def query(self, l, r):
        self._push_to(l + self.size - 1)
        self._push_to(r + self.size - 1)
        res1 = 0
        res2 = 0
        length = 0
        l += self.size - 1
        r += self.size - 1
        while l <= r:
            if l & 1 == 1:
                res1 = (res1 * self.pow1[self._len(l)] + self.hash1[l]) % MOD1
                res2 = (res2 * self.pow2[self._len(l)] + self.hash2[l]) % MOD2
                length += self._len(l)
                l += 1
            if r & 1 == 0:
                res1 = (res1 * self.pow1[self._len(r)] + self.hash1[r]) % MOD1
                res2 = (res2 * self.pow2[self._len(r)] + self.hash2[r]) % MOD2
                length += self._len(r)
                r -= 1
            l >>= 1
            r >>= 1
        return (res1, res2, length)

def lcp(st, a, b, maxlen):
    low, high = 0, maxlen+1
    while low + 1 < high:
        mid = (low + high)//2
        h1 = st.query(a, a+mid-1)
        h2 = st.query(b, b+mid-1)
        if h1[:2] == h2[:2]:
            low = mid
        else:
            high = mid
    return low

N = int(input())
U = input().rstrip()
Q = int(input())
st = SegmentTree(U)

for _q in range(Q):
    query = input().split()
    if query[0] == 'set':
        x, y, z = int(query[1]), int(query[2]), query[3]
        st.update(x, y, z)
    else:
        a, b, c, d = map(int, query[1:])
        len1 = b - a + 1
        len2 = d - c + 1
        length = min(len1, len2)
        p = lcp(st, a, c, length)
        if p == length:
            print('e' if len1 == len2 else 's' if len1 < len2 else 't')
        else:
            ch1 = st.query(a+p, a+p)
            ch2 = st.query(c+p, c+p)
            print('s' if ch1 < ch2 else 't')