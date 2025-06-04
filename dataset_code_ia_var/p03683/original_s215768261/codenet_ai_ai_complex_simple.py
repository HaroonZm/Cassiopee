from math import perm, prod
from functools import reduce
from operator import mul
from sys import stdin

MOD = 10**9 + 7

fact = lambda k: reduce(mul, range(1, k+1), 1)
modfact = lambda k: pow(prod(range(1, k+1)), 1, MOD)

def select_fn(is_eq, is_neigh):
    return (lambda n, m: print(((modfact(n) * modfact(m) * 2) % MOD))
            if is_eq else (lambda n, m: print((modfact(n) * modfact(m)) % MOD))
            if is_neigh else (lambda n, m: print(0)))

def main():
    [N, M], eq, neigh = map(int, stdin.readline().split()), lambda x, y: x==y, lambda x, y: abs(x-y)==1
    pick = select_fn(eq(N,M), neigh(N,M))
    pick(N, M)

if __name__ == "__main__":
    main()