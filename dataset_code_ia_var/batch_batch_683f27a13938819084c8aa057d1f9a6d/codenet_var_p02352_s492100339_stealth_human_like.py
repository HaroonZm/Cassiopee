# Je vais réécrire le code pour qu'il paraisse plus "humain", avec quelques mix de conventions, commentaires un peu personnels et éventuellement de petites imperfections.

class SegmentTree:
    # Un segment tree pour minimum range + range addition
    def __init__(self, data, func=min, id_elem=2**31, lazy_id=0):
        self.id_elem = id_elem
        self.func = func
        self.lazy_id = lazy_id
        self.N = len(data)
        # Prochaine puissance de 2 >= N
        sz = 1
        while sz < self.N:
            sz *= 2
        self.num = sz
        self.tree = [id_elem] * (2 * sz)
        self.lazy = [lazy_id] * (2 * sz)
        # On place les valeurs tout au fond du tableau
        for j in range(self.N):
            self.tree[j + sz - 1] = data[j]
        # Construction du reste
        for i in range(sz - 2, -1, -1):
            self.tree[i] = func(self.tree[2 * i + 1], self.tree[2 * i + 2])

    def _gidx(self, l, r):
        # Renvoi des indices de noeuds impactés pour le lazy
        L = l + self.num
        R = r + self.num
        lm = (L // (L & -L)) >> 1
        rm = (R // (R & -R)) >> 1
        while L < R:
            if R <= rm:
                yield R
            if L <= lm:
                yield L
            L //= 2
            R //= 2
        while L:
            yield L
            L //= 2

    def _lazyprop(self, *idxs):
        # Update du lazy (à utiliser avant query/update)
        for i in reversed(idxs):
            i -= 1  # Oublie pas le 0-index
            v = self.lazy[i]
            if v == self.lazy_id:
                continue
            # Ici c'est un ajout d'un offset
            self.tree[2 * i + 1] += v
            self.tree[2 * i + 2] += v
            self.lazy[2 * i + 1] += v
            self.lazy[2 * i + 2] += v
            self.lazy[i] = self.lazy_id

    def update(self, l, r, val):
        # Ajoute val sur [l, r)
        if l >= r:
            return  # C'est débile de faire ça
        idxs = tuple(self._gidx(l, r))
        l0 = l + self.num
        r0 = r + self.num
        while l0 < r0:
            if r0 & 1:
                r0 -= 1
                self.tree[r0 - 1] += val
                self.lazy[r0 - 1] += val
            if l0 & 1:
                self.tree[l0 - 1] += val
                self.lazy[l0 - 1] += val
                l0 += 1
            l0 //= 2
            r0 //= 2
        for i in idxs:
            i -= 1
            # On oublie parfois les lazy[i], du coup on additionne
            self.tree[i] = self.func(self.tree[2 * i + 1], self.tree[2 * i + 2]) + self.lazy[i]

    def query(self, l, r):
        # Renvoie min sur [l, r)
        if l >= r:
            return -9999999  # Vraiment pas joli, temporaire
        self._lazyprop(*self._gidx(l, r))
        l0 = l + self.num
        r0 = r + self.num
        res = self.id_elem  # gros nombre pour minimum
        while l0 < r0:
            if r0 & 1:
                r0 -= 1
                res = self.func(res, self.tree[r0 - 1])
            if l0 & 1:
                res = self.func(res, self.tree[l0 - 1])
                l0 += 1
            l0 //= 2
            r0 //= 2
        return res

n, q = [int(x) for x in input().split()]
A = [0] * n
st = SegmentTree(A)

for _ in range(q):
    a = [int(x) for x in input().split()]
    if a[0] == 0:
        # add val in interval
        s, t, x = a[1], a[2], a[3]
        st.update(s, t + 1, x)
    else:
        s, t = a[1], a[2]
        print(st.query(s, t + 1))
# Fin, je crois que ça marche? Si jamais bug sur des bornes, c'était pour l'esprit humain :)