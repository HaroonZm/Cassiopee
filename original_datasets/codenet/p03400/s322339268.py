import numpy as np

n = int(input())
d, x = map(int, input().split())

for i in range(n):
  a = int(input())
  k = np.floor((d-1)/a) + 1
  x += k

print(int(x))