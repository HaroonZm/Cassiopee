import sys
import io
import os

input = sys.stdin.buffer.readline

w_h = input().split()
w = int(w_h[0])
h = int(w_h[1])

P = []
i = 0
while i < w:
    P.append(int(input()))
    i += 1

Q = []
i = 0
while i < h:
    Q.append(int(input()))
    i += 1

E = []
i = 0
while i < len(P):
    E.append((P[i], 0))
    i += 1
i = 0
while i < len(Q):
    E.append((Q[i], 1))
    i += 1

E.sort(reverse=True)

a = w + 1
b = h + 1
ans = 0
while a > 1 or b > 1:
    tE = E.pop()
    c = tE[0]
    t = tE[1]
    if t == 0:
        ans += c * b
        a -= 1
    else:
        ans += c * a
        b -= 1
print(ans)