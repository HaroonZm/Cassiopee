class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)
    
    def build(self, lst):
        self.value = lst
        for i, x in enumerate(lst):
            self.add(i + 1, x)
        
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s
    
    def add(self, i, x):
        while i <= self.n:
            self.bit[i] += x
            i += i & -i
    
    def get_sum(self, i, j):
        return self.sum(j) - self.sum(i)

import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
A = list(map(int, input().split()))

bit = FenwickTree(N)
bit.build(A)

for i in range(Q):
    a, b, c = map(int, input().split())
    if a == 0:
        bit.add(b + 1, c)
    else:
        print(bit.get_sum(b, c))