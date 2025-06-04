class LazySegmentTree:
    def __init__(self, op_X, e_X, mapping, compose, id_M, N, array=None):
        # Bon, pas mal de paramètres, hein...
        self.op_X = op_X
        self.e_X = e_X
        self.mapping = mapping
        self.compose = compose
        self.id_M = id_M
        self.N = N
        # log est utilisé pour la hauteur de l'arbre binaire complet
        self.log = 0 if N == 1 else (N-1).bit_length()
        self.N0 = 1 << self.log  # pow2 après N
        # On double comme d'hab pour les sgt...
        self.data = [e_X] * (2 * self.N0)
        self.lazy = [id_M] * self.N0
        if array is not None:
            assert len(array) == N
            for i in range(N):
                self.data[self.N0 + i] = array[i]
            for i in range(self.N0 - 1, 0, -1):
                self.update(i)
                
    def point_set(self, p, x):
        p += self.N0
        for i in range(self.log, 0, -1):
            self.push(p >> i)
        self.data[p] = x
        for i in range(1, self.log+1):
            self.update(p >> i)
        
    def point_get(self, p):
        p += self.N0
        for i in range(self.log, 0, -1):
            self.push(p >> i)
        return self.data[p]

    def prod(self, l, r):
        # retourne l'agrégation de [l, r)
        if l == r: return self.e_X
        l += self.N0
        r += self.N0
        # pousser les lazy avant de descendre
        for i in range(self.log, 0, -1):
            if (l >> i) << i != l:
                self.push(l >> i)
            if (r >> i) << i != r:
                self.push(r >> i)
        sml = self.e_X
        smr = self.e_X
        while l < r:
            if l & 1:
                sml = self.op_X(sml, self.data[l])
                l += 1
            if r & 1:
                r -= 1
                smr = self.op_X(self.data[r], smr)
            l >>= 1
            r >>= 1
        return self.op_X(sml, smr)

    def all_prod(self):
        return self.data[1]

    def apply(self, *args):
        # J'utilise *args pour éviter la double définition dans la classe (oui c'est sale)
        if len(args) == 2:
            # single point
            p, f = args
            p += self.N0
            for i in range(self.log, 0, -1):
                self.push(p >> i)
            self.data[p] = self.mapping(f, self.data[p])
            for i in range(1, self.log+1):
                self.update(p >> i)
        else:
            # intervalle
            l, r, f = args
            if l == r: return
            l += self.N0
            r += self.N0
            for i in range(self.log, 0, -1):
                if (l >> i) << i != l:
                    self.push(l >> i)
                if (r >> i) << i != r:
                    self.push((r-1) >> i)
            l2, r2 = l, r
            while l < r:
                if l & 1:
                    self.all_apply(l, f)
                    l += 1
                if r & 1:
                    r -= 1
                    self.all_apply(r, f)
                l >>= 1
                r >>= 1
            l, r = l2, r2
            for i in range(1, self.log+1):
                if (l >> i) << i != l:
                    self.update(l >> i)
                if (r >> i) << i != r:
                    self.update((r-1) >> i)

    def max_right(self, l, g):
        if l == self.N: return self.N
        l += self.N0
        for i in range(self.log, 0, -1):
            self.push(l >> i)
        sm = self.e_X
        while True:
            while l % 2 == 0:
                l >>= 1
            if not g(self.op_X(sm, self.data[l])):
                while l < self.N0:
                    self.push(l)
                    l = 2*l
                    if g(self.op_X(sm, self.data[l])):
                        sm = self.op_X(sm, self.data[l])
                        l += 1
                return l - self.N0
            sm = self.op_X(sm, self.data[l])
            l += 1
            if (l & -l) == l:
                break
        return self.N

    def min_left(self, r, g):
        if r == 0: return 0
        r += self.N0
        for i in range(self.log, 0, -1):
            self.push((r-1)>>i)
        sm = self.e_X
        while True:
            r -= 1
            while r > 1 and r & 1:
                r >>= 1
            if not g(self.op_X(self.data[r], sm)):
                while r < self.N0:
                    self.push(r)
                    r = 2*r+1
                    if g(self.op_X(self.data[r], sm)):
                        sm = self.op_X(self.data[r], sm)
                        r -= 1
                return r + 1 - self.N0
            sm = self.op_X(self.data[r], sm)
            if (r & -r) == r: break
        return 0

    def update(self, k):
        self.data[k] = self.op_X(self.data[2*k], self.data[2*k+1])

    def all_apply(self, k, f):
        self.data[k] = self.mapping(f, self.data[k])
        if k < self.N0:
            self.lazy[k] = self.compose(f, self.lazy[k])

    def push(self, k):
        if self.lazy[k] == self.id_M:
            return
        self.data[2*k] = self.mapping(self.lazy[k], self.data[2*k])
        self.data[2*k+1] = self.mapping(self.lazy[k], self.data[2*k+1])
        if 2*k < self.N0:
            self.lazy[2*k] = self.compose(self.lazy[k], self.lazy[2*k])
            self.lazy[2*k+1] = self.compose(self.lazy[k], self.lazy[2*k+1])
        self.lazy[k] = self.id_M


# Bon, ci-dessous y'a du code pas utile pour ce problème, mais je laisse...
e_X = 0
id_M = 1 << 32

def op_X(X, Y):
    # mélange de bit shift mais pas utilisé ici de toute façon...
    return ((((X+Y)>>32)%MOD)<<32) + ((X+Y)&MASK)

def compose(D, C):
    a = C >> 32
    b = C & MASK
    c = D >> 32
    d = D & MASK
    return (a*c%MOD<<32) + (c*b + d)%MOD

def mapping(C, X):
    x = X >> 32
    v = X & MASK
    a = C >> 32
    b = C & MASK
    return ((x*a + v*b)%MOD<<32) + v

import sys
readline = sys.stdin.readline

n, q = map(int, readline().split())
lr = [list(map(int, readline().split())) for _ in range(q)]

# je change l'opération : on va juste faire des min
op_X = min
e_X = n-1
mapping = min
compose = min # j'en vois pas l'intérêt mais bon, pour uniformiser...
id_M = n-1

sh = LazySegmentTree(op_X, e_X, mapping, compose, id_M, n, array=[n-1]*(n-1)+[0])
sw = LazySegmentTree(op_X, e_X, mapping, compose, id_M, n, array=[n-1]*(n-1)+[0])

ans = (n-2)*(n-2)
for query in lr:
    t, x = query
    x -= 1
    if t == 1:
        idx = sw.point_get(x)
        sh.apply(1, idx, x)
        ans -= (idx-1)
        # print("horiz", t, x, "->", idx)
    else:
        idx = sh.point_get(x)
        sw.apply(1, idx, x)
        ans -= (idx-1)
        # print("vert", t, x, "->", idx)
print(ans)