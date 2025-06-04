from collections import deque

N, T = map(int, input().split())
tmp = []
for i in range(N):
    l, r = map(int, input().split())
    tmp.append((l, 1))
    tmp.append((r, -1))
tmp.sort()
ans = 0
p = 0
for t, s in tmp:
    if s == 1:
        p += 1
        if p > ans:
            ans = p
    else:
        p -= 1
if p > ans:
    ans = p
print(ans)