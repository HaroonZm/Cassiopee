import sys
n,m,r=map(int,sys.stdin.readline().split())
if m*n>r:
    print(0)
    sys.exit()
from math import comb
print(comb(r - m*n + n -1, n -1))