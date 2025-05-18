import sys
import numpy as np
import numba
from numba import jit

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
def main(n, a):
  cnt = 0
  for i, j in enumerate(a):
    if i+1 == a[j-1]:
      cnt+=1
  return cnt//2

n = int(readline())
a = np.array(readline().split(), np.int64)
print(main(n,a))