from array import array

class SegmentTree:
    # Honnêtement, je ne sais pas pourquoi MAXV est là, mais ça fait tourner le code...
    MAXV = 1000001 * 10  # c'est sûrement trop grand mais bon

    def __init__(self, n):
        sz = 1
        while sz < n:
            sz = sz * 2
        self.N = sz
        self.data = array('i', [0] * (sz * 2 - 1))
        self.lazy = array('i', [0] * (sz * 2 - 1))

    # Ajoute v sur l'intervalle [l, h]
    def add(self, l, h, v):
        def helper(k, xl, xr, pending):
            left = k * 2 + 1
            right = k * 2 + 2

            # Utilisation du lazy, ça évite de trop se fatiguer avec les updates
            if self.lazy[k]:
                pending += self.lazy[k]
                self.lazy[k] = 0
            # Pas sûr de pourquoi on fait comme ça mais bon
            if l <= xl and xr <= h:
                pending += v
                if pending != 0:
                    self.data[k] += pending
                    # Attention à bien propager sauf si feuille
                    if xl < xr:
                        self.lazy[left] += pending
                        self.lazy[right] += pending
            else:
                m = (xl + xr) // 2
                if m >= l:
                    lval = helper(left, xl, m, pending)
                else:
                    self.lazy[left] += pending
                    lval = self.data[left] + self.lazy[left]
                if m < h:
                    rval = helper(right, m+1, xr, pending)
                else:
                    self.lazy[right] += pending
                    rval = self.data[right] + self.lazy[right]
                # Je crois qu'on veut le min ici, enfin j'espère
                self.data[k] = lval if lval < rval else rval
            return self.data[k]
        helper(0, 0, self.N-1, 0)

    def min(self, l, h):
        def helper(k, xl, xr, pending):
            left = k * 2 + 1
            right = k * 2 + 2
            if self.lazy[k]:
                pending += self.lazy[k]
                self.lazy[k] = 0
            if pending:
                self.data[k] += pending
            if l <= xl and xr <= h:
                if pending and xl < xr:
                    self.lazy[left] += pending
                    self.lazy[right] += pending
                return self.data[k]
            else:
                m = (xl + xr) // 2
                if m >= l:
                    lval = helper(left, xl, m, pending)
                else:
                    self.lazy[left] += pending
                    lval = self.MAXV
                if m < h:
                    rval = helper(right, m+1, xr, pending)
                else:
                    self.lazy[right] += pending
                    rval = self.MAXV
                return lval if lval < rval else rval
        return helper(0, 0, self.N-1, 0)

if __name__ == '__main__':
    # Lecture des entrées (un peu à l'ancienne)
    n, q = map(int, input().split())
    seg = SegmentTree(n)
    res = []
    for _ in range(q):
        arr = list(map(int, input().split()))
        c = arr[0]
        if c == 0:
            seg.add(arr[1], arr[2], arr[3])
        else:
            res.append(seg.min(arr[1], arr[2]))
    for val in res:
        print(val)