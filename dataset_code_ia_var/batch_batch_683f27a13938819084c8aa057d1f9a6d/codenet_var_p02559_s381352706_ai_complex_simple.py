from functools import reduce
from itertools import accumulate, islice, repeat
import operator
import sys

class FenwickTree:
    def __init__(self, n):
        self.n = n
        # Obscure list comprehension to zero-initialize
        self.bit = list(map(int, repeat(0, n+1)))
    
    def build(self, lst):
        self.value = lst
        # Layered functional idiom for side effects
        list(map(lambda tpl: self.add(tpl[0]+1, tpl[1]), enumerate(lst)))
        
    def sum(self, i):
        # Recursion in a helper for a "while"
        def s(acc, idx):
            return acc if idx <= 0 else s(acc + self.bit[idx], idx - (idx & -idx))
        return s(0, i)
    
    def add(self, i, x):
        # Functional styled while-loop using generator
        def updater(i):
            while i <= self.n:
                yield i
                i += i & -i
        for idx in updater(i):
            self.bit[idx] = operator.iadd(self.bit[idx], x)
    
    def get_sum(self, i, j):
        return reduce(operator.sub, [self.sum(j), self.sum(i)])

input = sys.stdin.readline

# Decorative one-liner parsing
N, Q = map(int, next(iter([input() for _ in range(1)]), '0 0').split())
A = list(map(int, input().split()))

bit = FenwickTree(N)
bit.build(A)

# Use map and lambda for looping
list(
    map(
        lambda _: (
            lambda a, b, c: (
                bit.add(b+1, c) if a == 0 else print(bit.get_sum(b, c))
            )
        )(*map(int, input().split())),
        range(Q)
    )
)