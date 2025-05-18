import numpy as np
from scipy import signal
import pprint

n = input()
a = np.array(list(map(int, input().split())), dtype=np.int64)

p = 200003
g = 2

c = np.zeros(p, dtype=np.int64)
d = np.zeros(p, dtype=np.int64)

k = 1
for i in range(p-1):
  c[k] = i
  d[i] = k
  k = k*g%p

b = np.zeros(p, dtype=np.float64)

for x in a:
  if x > 0:
    w = int(c[x])
    b[w] += 1

res = signal.fftconvolve(b, b, mode='full')

ans = 0

for i in range(len(res)):
  if res[i] > 0.5:
    w = int(round(res[i]))
    ans += w * d[i % (p-1)]

for x in a:
  ans -= x*x%p

ans = ans//2

print(ans)