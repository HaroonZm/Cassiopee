import math
import string
import itertools
import fractions
import heapq
import collections
import re
import array
import bisect
import sys
import random
import time
import copy
import functools

def set_recursion():
    sys.setrecursionlimit(10**7)

def get_inf():
    return 10**20

def get_eps():
    return 1.0 / 10**13

def get_mod():
    return 10**9+7

def get_dd():
    return [(-1,0),(0,1),(1,0),(0,-1)]

def get_ddn():
    return [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI():
    return [int(x) for x in sys.stdin.readline().split()]

def LI_():
    return [int(x)-1 for x in sys.stdin.readline().split()]

def LF():
    return [float(x) for x in sys.stdin.readline().split()]

def LS():
    return sys.stdin.readline().split()

def I():
    return int(sys.stdin.readline())

def F():
    return float(sys.stdin.readline())

def S():
    return input()

def pf(s):
    return print(s, flush=True)

def M(n):
    return ModInt(n)

def powmod(x, y, mod):
    return pow(x, y, mod)

def joinln(seq):
    return '\n'.join(map(str,seq))

def break_cond(n):
    return n == 0

def ords(s):
    return [ord(c) for c in s]

# Fragmentation for ModInt
def modint_init(self, n):
    self.n = n

def modint_xn(x):
    if isinstance(x, ModInt):
        return x.n
    return x

def modint_add(self, x):
    x = modint_xn(x)
    return ModInt((self.n + x) % get_mod())

def modint_sub(self, x):
    x = modint_xn(x)
    return ModInt((self.n - x) % get_mod())

def modint_mul(self, x):
    x = modint_xn(x)
    return ModInt((self.n * x) % get_mod())

def modint_truediv(self, x):
    x = modint_xn(x)
    return ModInt(self.n * powmod(x, get_mod()-2, get_mod()) % get_mod())

def modint_str(self):
    return str(self.n)

class ModInt():
    def __init__(self, n):
        modint_init(self, n)
    def __add__(self, x):
        return modint_add(self, x)
    def __sub__(self, x):
        return modint_sub(self, x)
    def __mul__(self, x):
        return modint_mul(self, x)
    def __truediv__(self, x):
        return modint_truediv(self, x)
    @classmethod
    def xn(cls, x):
        return modint_xn(x)
    def __str__(self):
        return modint_str(self)

# --- RollingHash fragmentation --- 
def rollinghash_init_build_arrays(s):
    a = ords(s)
    a1 = [M(a[0])]
    a2 = [M(a[0])]
    rollinghash_extend(a, a1, a2)
    return len(s), a1, a2

def rollinghash_extend(a, a1, a2):
    for c in a[1:]:
        a1.append(a1[-1] * 997 + c)
        a2.append(a2[-1] * 991 + c)

def rollinghash_init(self, s):
    N, A1, A2 = rollinghash_init_build_arrays(s)
    self.N = N
    self.A1 = A1
    self.A2 = A2

def rollinghash_get_t1(A1, l, r):
    return (A1[r] - A1[l-1] * powmod(997, r-l+1, get_mod())).n

def rollinghash_get_t2(A2, l, r):
    return (A2[r] - A2[l-1] * powmod(991, r-l+1, get_mod())).n

def rollinghash_get(self, l, r):
    if l == 0:
        return (self.A1[r].n, self.A2[r].n)
    t1 = rollinghash_get_t1(self.A1, l, r)
    t2 = rollinghash_get_t2(self.A2, l, r)
    return (t1, t2)

class RollingHash():
    def __init__(self, s):
        rollinghash_init(self, s)
    def get(self, l, r):
        return rollinghash_get(self, l, r)

# --- fragmentation for f() ---
def f_read_s():
    return S()

def f_read_qa(m):
    return [S() for _ in range(m)]

def f_process_queries(qa, l, r, rs):
    for q in qa:
        l, r = f_update_indices(l, r, q)
        rs.add((l, r))
    return rs

def f_update_indices(l, r, q):
    if q == 'L++':
        l += 1
    elif q == 'L--':
        l -= 1
    elif q == 'R++':
        r += 1
    else:
        r -= 1
    return l, r

def f_hash_ranges(rs, rh):
    rrs = set()
    for l, r in rs:
        rrs.add(rh.get(l, r))
    return rrs

def f_count_unique(rrs):
    return len(rrs)

def f(n, m):
    rs = set()
    s = f_read_s()
    qa = f_read_qa(m)
    l = 0
    r = 0
    rh = RollingHash(s)
    rs = f_process_queries(qa, l, r, rs)
    rrs = f_hash_ranges(rs, rh)
    ans = f_count_unique(rrs)
    return ans

def main_loop(rr):
    while True:
        n, m = LI()
        if break_cond(n):
            break
        rr.append(f(n, m))
        break

def main():
    set_recursion()
    inf = get_inf()
    eps = get_eps()
    mod = get_mod()
    dd = get_dd()
    ddn = get_ddn()
    rr = []
    main_loop(rr)
    return joinln(rr)

print(main())