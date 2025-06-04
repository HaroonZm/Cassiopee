import sys
from sys import stdin
import numpy as np

def get_input():
    return stdin.readline()

def setup(H,W,D):
    arrx = np.arange(H)
    arry = np.arange(W)
    add = np.add.outer(arrx, arry)
    sub = np.subtract.outer(arrx, arry)
    # Opérations façon impérative
    for mat in (add, sub):
        mat //= D; mat %= 2
    return add, sub

class CGrid:
    def __init__(self, h, w):
        self.data = np.zeros((h, w), dtype='U1')
    def fill(self, mask, val):
        np.putmask(self.data, mask, val)
    def __iter__(self):
        return iter(self.data)

H, W, D = list(map(int, get_input().split()))
p, m = setup(H, W, D)
ind = p + 2*m

cg = CGrid(H, W)
for val, let in enumerate(['R','B','G','Y']):
    cg.fill(ind==val, let)

for row in cg:
    res = []
    i = 0
    while i < len(row):
        res.append(row[i])
        i += 1
    print(''.join(res))