import sys
import io, os
input = sys.stdin.buffer.readline
#input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline

w, h = map(int, input().split())
P = [int(input()) for _ in range(w)]
Q = [int(input()) for _ in range(h)]

E = []
for p in P:
    E.append((p, 0))
for q in Q:
    E.append((q, 1))
E.sort(reverse=True)

a = w+1
b = h+1
ans = 0
while a >1 or b > 1:
    c, t = E.pop()
    if t == 0:
        ans += c*b
        a -= 1
    else:
        ans += c*a
        b -= 1
print(ans)