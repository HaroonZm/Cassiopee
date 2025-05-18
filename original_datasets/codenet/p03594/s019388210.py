import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

import numpy as np

H,W,D = map(int,input().split())

x = np.arange(H); y = np.arange(W)
plus = x[:,None] + y[None,:]
minus = x[:,None] - y[None,:]
plus //= D; plus %= 2
minus //= D; minus %= 2

x = plus + 2*minus
grid = np.zeros((H,W),dtype='U1')
grid[x==0] = 'R'
grid[x==1] = 'B'
grid[x==2] = 'G'
grid[x==3] = 'Y'

print('\n'.join(''.join(x for x in row) for row in grid))