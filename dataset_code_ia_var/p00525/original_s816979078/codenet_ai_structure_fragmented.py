import math
from collections import UserList
from operator import itemgetter
import sys

def get_depth(n):
    return math.ceil(math.log(n, 2))

def get_size(depth):
    return 1 << depth

def create_bit_array(size):
    return [0] * 2 * size

def create_renew_array(size):
    return [0] * 2 * size

def seg_tree_add_loop(self, p, v):
    p += self.size
    while p:
        self.bit[p] += v
        p >>= 1

def seg_tree_query_loop(self, l, r):
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

def seg_tree_set_renew_loop(self, l, r):
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

def seg_tree_is_renew_loop(self, p):
    p += self.size
    while p:
        if self.renew[p]:
            return True
        p >>= 1
    return False

def seg_tree_unset_renew_loop(self, p):
    p += self.size
    for i in range(self.depth - 1, 0, -1):
        idx = p >> i
        if self.renew[idx]:
            self.renew[idx] = 0
            self.renew[(idx)*2] = 1
            self.renew[(idx)*2+1] = 1
    self.renew[p] = 0

def seg_tree_get_lf_loop(self, r):
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

class seg_tree:
    def __init__(self, n):
        self.depth = get_depth(n)
        self.size = get_size(self.depth)
        self.bit = create_bit_array(self.size)
        self.renew = create_renew_array(self.size)
    def add(self, p, v):
        seg_tree_add_loop(self, p, v)
    def query(self, l, r):
        return seg_tree_query_loop(self, l, r)
    def set_renew(self, l, r):
        seg_tree_set_renew_loop(self, l, r)
    def is_renew(self, p):
        return seg_tree_is_renew_loop(self, p)
    def unset_renew(self, p):
        seg_tree_unset_renew_loop(self, p)
    def get_lf(self, r):
        return seg_tree_get_lf_loop(self, r)

def uf_base_init(self):
    UserList.__init__(self)

def uf_root_rec(self, p):
    if self.data[p] < 0:
        return p
    self.data[p] = self.root(self.data[p])
    return self.data[p]

def uf_join_logic(self, p, q):
    p, q = self.root(p), self.root(q)
    if p == q:
        return False
    if self.data[p] < self.data[q]:
        p, q = q, p
    self.data[p], self.data[q] = self.data[q], p
    return True

class union_find(UserList):
    def __init__(self):
        uf_base_init(self)
    def root(self, p):
        return uf_root_rec(self, p)
    def join(self, p, q):
        return uf_join_logic(self, p, q)

def bisect(a,v):
    l, r = 0, len(a)
    while l < r:
        m = (l + r) // 2
        if a[m] < v:
            l = m + 1
        else:
            r = m
    return l

def do_adjust(seg, uf, target, p):
    if seg.is_renew(p):
        uf.append(-1)
        seg.unset_renew(p)
        target[p] = len(uf) - 1

def read_whn(f):
    w,h,n = map(int, f.readline().split())
    return w,h,n

def read_abcd_lines(f):
    return [list(map(int,line.split())) for line in f]

def extend_abcd(abcd, w, h):
    abcd.extend([[0,0,w,0], [0,0,0,h], [w,0,w,h], [0,h,w,h]])
    return abcd

def get_xs(abcd):
    all_x = [abcdi[0] for abcdi in abcd] + [abcdi[2] for abcdi in abcd] + [-1]
    xs = {x:i for i, x in enumerate(sorted(set(all_x)))}
    return xs

def remap_abcd(abcd, xs):
    return [(xs[a], b, xs[c], d) for a,b,c,d in abcd]

def create_target(n):
    return [-1]*n*2

def init_target(target):
    target[0] = 0
    return target

def create_union_find():
    uf = union_find()
    uf.append(-1)
    return uf

def create_segment_tree(xs):
    return seg_tree(len(xs))

def add_initial_segment(seg):
    seg.add(0, 1)

def create_action_list(abcd):
    a = []
    for x1, y1, x2, y2 in abcd:
        if x1 == x2:
            a.append((y1, 0, x1, -1))
            a.append((y2, 2, x1, -1))
        else:
            a.append((y1, 1, x1, x2))
    return a

def sort_action_list(a):
    a.sort(key=itemgetter(0,1))
    return a

def process_action_add(seg, uf, target, left):
    lf = seg.get_lf(left)
    do_adjust(seg, uf, target, lf)
    do_adjust(seg, uf, target, left)
    target[left] = target[lf]
    seg.add(left, 1)
    return

def process_action_query(seg, uf, target, left, right, ret):
    count = seg.query(left, right+1)
    if count < 2:
        return ret
    ret += count - 1
    seg.set_renew(left, seg.get_lf(right+1))
    return ret

def process_action_remove(seg, uf, target, left, ret):
    lf = seg.get_lf(left)
    do_adjust(seg, uf, target, lf)
    do_adjust(seg, uf, target, left)
    if uf.join(target[lf], target[left]):
        ret -= 1
    seg.add(left, -1)
    return ret

def main_loop(a, seg, uf, target):
    ret = 0
    for _, act, left, right in a:
        if act == 0:
            process_action_add(seg, uf, target, left)
        elif act == 1:
            ret = process_action_query(seg, uf, target, left, right, ret)
        elif act == 2:
            ret = process_action_remove(seg, uf, target, left, ret)
    return ret

def main(f):    
    w, h, n = read_whn(f)
    abcd = read_abcd_lines(f)
    abcd = extend_abcd(abcd, w, h)
    xs = get_xs(abcd)
    abcd = remap_abcd(abcd, xs)
    target = create_target(n)
    target = init_target(target)
    uf = create_union_find()
    seg = create_segment_tree(xs)
    add_initial_segment(seg)
    a = create_action_list(abcd)
    a = sort_action_list(a)
    ret = main_loop(a, seg, uf, target)
    print(ret)

f = sys.stdin
main(f)