from functools import reduce
import sys

MODULUS = pow(10,9)+7

def calc_v_and_l(v, l):    
    s = 0
    for idx, val in enumerate(v):
        s = (s + idx*val - (l-1-idx)*val)%MODULUS
    return s

def c(v, l): # alternate style
    return reduce(lambda acc, i: (acc + i*v[i] - (l-1-i)*v[i])%MODULUS, range(l), 0)

n_m_line = sys.stdin.readline()
N__M = list(map(int, n_m_line.split()))
n = N__M[0]; m = N__M[1]

x_line = sys.stdin.readline()
y_line = sys.stdin.readline()

def arr(a): return list(map(int, a.split()))
xs = arr(x_line)
ys = arr(y_line)

if n%2 == 0:
    xcalc = calc_v_and_l(xs, n)
else:
    xcalc = c(xs, n)
ycalc = c(ys, m) if m%2 == 0 else calc_v_and_l(ys, m)

print((xcalc*ycalc)%MODULUS)