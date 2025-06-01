import math
import sys
from collections import UserList

w,h,n = map(int,sys.stdin.readline().split())
abcd = [list(map(int,line.split())) for line in sys.stdin]

abcd.extend([[0,0,w,0],[0,0,0,h],[w,0,w,h],[0,h,w,h]])

xs_values = [abcdi[0] for abcdi in abcd] + [abcdi[2] for abcdi in abcd] + [-1]
xs_sorted = sorted(set(xs_values))
xs = {}
for i,x in enumerate(xs_sorted):
    xs[x] = i
for i in range(len(abcd)):
    a,b,c,d = abcd[i]
    abcd[i] = (xs[a], b, xs[c], d)

target = [-1] * (n*2)
target[0] = 0

depth = math.ceil(math.log(len(xs_sorted), 2))
size = 1 << depth
bit = [0] * (2*size)
renew = [0] * (2*size)

def bit_add(p,v):
    p += size
    while p > 0:
        bit[p] += v
        p >>= 1

def bit_query(l,r):
    l += size
    r += size
    ret = 0
    while l < r:
        if l & 1:
            ret += bit[l]
            l += 1
        if r & 1:
            r -= 1
            ret += bit[r]
        l >>= 1
        r >>= 1
    return ret

def renew_set(l,r):
    l += size
    r += size
    while l < r:
        if l & 1:
            renew[l] = 1
            l += 1
        if r & 1:
            r -= 1
            renew[r] = 1
        l >>= 1
        r >>= 1

def renew_is(p):
    p += size
    while p > 0:
        if renew[p]:
            return True
        p >>= 1
    return False

def renew_unset(p):
    p += size
    for i in range(depth - 1, 0, -1):
        node = p >> i
        if renew[node]:
            renew[node] = 0
            renew[node*2] = 1
            renew[node*2 + 1] = 1
    renew[p] = 0

def get_lf(r):
    l = size
    r += size
    while l < r:
        if r & 1:
            r -= 1
            if bit[r]:
                node = r
                while node < size:
                    node <<= 1
                    if bit[node+1]:
                        node += 1
                return node - size
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
        p = self.root(p)
        q = self.root(q)
        if p == q:
            return False
        if self.data[p] < self.data[q]:
            p, q = q, p
        self.data[p],self.data[q] = self.data[q], p
        return True

def adjust(p):
    if renew_is(p):
        uf.append(-1)
        renew_unset(p)
        target[p] = len(uf) - 1

uf = union_find()
uf.append(-1)

bit_add(0, 1)

a = []
for x1,y1,x2,y2 in abcd:
    if x1 == x2:
        a.append((y1, 0, x1, -1))
        a.append((y2, 2, x1, -1))
    else:
        a.append((y1, 1, x1, x2))
a.sort(key=lambda x: (x[0], x[1]))

ret = 0
for y, act, left, right in a:
    if act == 0:
        lf = get_lf(left)
        adjust(lf)
        adjust(left)
        target[left] = target[lf]
        bit_add(left, 1)
    elif act == 1:
        count = bit_query(left, right+1)
        if count < 2:
            continue
        ret += count - 1
        renew_set(left, get_lf(right + 1))
    else:
        lf = get_lf(left)
        adjust(lf)
        adjust(left)
        if uf.join(target[lf], target[left]):
            ret -= 1
        bit_add(left, -1)

print(ret)