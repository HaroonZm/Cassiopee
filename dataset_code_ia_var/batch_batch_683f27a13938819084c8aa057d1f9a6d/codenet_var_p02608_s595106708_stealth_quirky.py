from sys import stdin as _s
from math import sqrt as s_, ceil as c_

N = int(_s.readline())
A = [None] + [0] * N

Q = int(s_(N)) + (bool(s_(N) % 1))

for _a in range(1, Q + 1):
    for _b in range(1, Q + 1):
        for _c in range(1, Q + 1):
            _v = _a * _a + _b * _b + _c * _c + _a * _b + _b * _c + _c * _a
            if _v >= 1 and _v <= N:
                A[_v] += 1
for _k in list(range(1, N + 1)):
    print(A[_k])