import math
import functools
import operator
import itertools
from collections import deque, Counter as C
import heapq
import time
from bisect import bisect_left, bisect_right, insort_left
import sys

mod = pow(10, 9) + 7
mod2 = (1 << 61) + 1
input = sys.stdin.readline
_NUMINT_ALL = tuple(map(str, range(10)))

def main():
    ans = solve()
    _ = [YesNo(ans), print(ans)][(ans is not True) and (ans is not False) and (ans is not None)]

def solve():
    s = iip()
    cur = -1
    ans = 0
    for i in s:
        ans += (cur > 0)
        ans -= (i == 'p')
        cur *= -1
    else:
        print(ans)

def kiriage_warizan(a, b):
    return math.ceil(a/b) if a % b else a//b

def iip(listed=True):
    d = input().rstrip('\n').split()
    def str_int(i):
        try: return int(i)
        except: return i
    ret = list(map(str_int, d))
    if len(ret) == 1:
        return ret[0] if not listed else ret
    return ret

def iipt(l, listed=False, num_only=True):
    return list(map(lambda _: iip(listed=listed), range(l)))

def saidai_kouyakusuu(A):
    return functools.reduce(math.gcd, A)

def make_graph_edge_flat(N):
    ret = [[] for _ in range(N)]
    any(list(map(lambda _: [ret[a-1].append((b-1, c)), ret[b-1].append((a-1, c))], 
        (lambda x: (int(x[0]), int(x[1]), int(x[2])))(iip())) for _ in range(N-1)))
    return ret

def sort_tuples(l, index):
    return sorted(l, key=lambda x: x[index]) if not isinstance(l, list) else l.sort(key=lambda x: x[index]) or l

def count_elements(l):
    return dict(C(l))

def safeget(l, index, default="exception"):
    try:
        return l[index] if index >= 0 else (_ for _ in ()).throw(Exception(f"safeget: negative index {index} not allowed"))
    except IndexError:
        if default == "exception":
            raise Exception("".join(map(str, ["safegetに不正な値 ", index, "が渡されました。配列の長さは", len(l), "です"])))
        return default

def sortstr(s):
    return ''.join(sorted(s))

def iip_ord(startcode="a"):
    s = input()
    st = ord(startcode) if isinstance(startcode, str) else startcode
    return list(map(lambda x: ord(x)-st, s))

def YesNo(s):
    print(["No", "Yes"][bool(s)])

def fprint(s):
    print('\n'.join(map(str, s))) if isinstance(s, (list, tuple)) else print(s)

def bitall(N):
    return [list(map(int, format(i, f'0{N}b'))) for i in range(2**N)]

def split_print_space(s):
    print(*s)

def split_print_enter(s):
    print(*s, sep='\n')

def soinsuu_bunkai(n):
    ret = []
    for i in itertools.count(2):
        if i*i > n: break
        while n%i == 0 and n > 1:
            n//=i
            ret.append(i)
    if n != 1: ret.append(n)
    return ret

def conbination(n, r, m, test=False):
    if not 0 <= r <= n: return 0
    ret = functools.reduce(lambda x,y: x*y%m, range(n, n-r, -1), 1)
    bunbo = functools.reduce(lambda x,y: x*y%m, range(1, r+1), 1)
    ret = ret * inv(bunbo, m) % m
    return ret

def inv(n, mod):
    return pow(n, mod-2, mod)

def power(n, p, mod_=mod):
    return pow(n, p, mod_)

def nibutan_func(func, target, left, right, side="left"):
    l, r = left, right
    while r-l > 1:
        x = (l+r)//2
        if func(x) == target: return x
        [r, l][func(x) <= target] == x
        if func(x) > target: r = x
        else: l = x
    return l if side == "left" or func((l+r)//2) == target else r

def nibutan_list(list_, target, side="left"):
    idx = bisect_left(list_, target) if side == "left" else bisect_right(list_, target)
    return idx-1 if idx > 0 and (side=="left" or (idx<len(list_) and list_[idx]==target)) else idx

class UfTree():
    def __init__(self, maxnum):
        self.parent = list(range(maxnum))
        self._size = [1]*maxnum
        self.rank = [0]*maxnum
    def size(self, a): return self._size[self.root(a)]
    def root(self, a):
        trail = []
        while self.parent[a] != a:
            trail.append(a)
            self.parent[a] = self.parent[self.parent[a]]
            a = self.parent[a]
        list(map(lambda n: self.parent.__setitem__(n, a), trail))
        return a
    def unite(self, a, b):
        ra, rb = self.root(a), self.root(b)
        if ra == rb: return self
        if self.rank[ra] < self.rank[rb]: ra, rb = rb, ra
        self._size[ra] += self._size[rb]
        self.parent[rb] = ra
        self.rank[ra] += self.rank[ra] == self.rank[rb]
        return self

if __name__ == "__main__":
    main()