import math
from collections import UserList
from operator import itemgetter
import sys

class seg_tree:
    def __init__(self, n):
        self.depth = math.ceil(math.log(n, 2))
        self.size = 1 << self.depth
        self.bit = [0] * (2 * self.size)
        self.renew = [0] * (2 * self.size)

    def add(self, p, v):
        p += self.size
        while p:
            self.bit[p] += v
            p >>= 1

    def query(self, l, r):
        l += self.size
        r += self.size
        ret = 0
        while l < r:
            if l & 1:
                ret += self.bit[l]
                l += 1
            if r & 1:
                r -= 1
                ret += self.bit[r]
            l >>= 1
            r >>= 1
        return ret

    def set_renew(self, l, r):
        l += self.size
        r += self.size
        while l < r:
            if l & 1:
                self.renew[l] = 1
                l += 1
            if r & 1:
                r -= 1
                self.renew[r] = 1
            l >>= 1
            r >>= 1

    def is_renew(self, p):
        p += self.size
        while p:
            if self.renew[p]:
                return True
            p >>= 1
        return False

    def unset_renew(self, p):
        p += self.size
        for i in range(self.depth - 1, 0, -1):
            if self.renew[p >> i]:
                self.renew[p >> i] = 0
                self.renew[(p >> i) * 2] = 1
                self.renew[(p >> i) * 2 + 1] = 1
        self.renew[p] = 0

    def get_lf(self, r):
        l = self.size
        r += self.size
        while l < r:
            if r & 1:
                r -= 1
                if self.bit[r]:
                    while r < self.size:
                        r <<= 1
                        if self.bit[r + 1]:
                            r += 1
                    return r - self.size
            if l & 1:
                l += 1
            l >>= 1
            r >>= 1
        return -1

class union_find(UserList):
    def __init__(self):
        UserList.__init__(self)

    def root(self, p):
        if self.data[p] < 0:
            return p
        self.data[p] = self.root(self.data[p])
        return self.data[p]

    def join(self, p, q):
        p, q = self.root(p), self.root(q)
        if p == q:
            return False
        if self.data[p] < self.data[q]:
            p, q = q, p
        self.data[p], self.data[q] = self.data[q], p
        return True

def bisect(a, v):
    l, r = 0, len(a)
    while l < r:
        m = (l + r) // 2
        if a[m] < v:
            l = m + 1
        else:
            r = m
    return l

def adjust(seg, uf, target, p):
    if seg.is_renew(p):
        uf.append(-1)
        seg.unset_renew(p)
        target[p] = len(uf) - 1

def main(f):
    w, h, n = map(int, f.readline().split())
    abcd = [list(map(int, line.split())) for line in f]

    abcd.extend([
        [0, 0, w, 0],
        [0, 0, 0, h],
        [w, 0, w, h],
        [0, h, w, h]
    ])

    xs = {x: i for i, x in enumerate(sorted(set(
        [abcdi[0] for abcdi in abcd] + [abcdi[2] for abcdi in abcd] + [-1]
    )))}
    abcd = [(xs[a], b, xs[c], d) for a, b, c, d in abcd]

    target = [-1] * (n * 2)
    target[0] = 0
    uf = union_find()
    uf.append(-1)
    seg = seg_tree(len(xs))
    seg.add(0, 1)

    a = []
    for x1, y1, x2, y2 in abcd:
        if x1 == x2:
            a.append((y1, 0, x1, -1))
            a.append((y2, 2, x1, -1))
        else:
            a.append((y1, 1, x1, x2))
    a.sort(key=itemgetter(0, 1))
    ret = 0
    for _, act, left, right in a:
        if act == 0:
            lf = seg.get_lf(left)
            adjust(seg, uf, target, lf)
            adjust(seg, uf, target, left)
            target[left] = target[lf]
            seg.add(left, 1)
        elif act == 1:
            count = seg.query(left, right + 1)
            if count < 2:
                continue
            ret += count - 1
            seg.set_renew(left, seg.get_lf(right + 1))
        elif act == 2:
            lf = seg.get_lf(left)
            adjust(seg, uf, target, lf)
            adjust(seg, uf, target, left)
            if uf.join(target[lf], target[left]):
                ret -= 1
            seg.add(left, -1)
    print(ret)

f = sys.stdin
main(f)