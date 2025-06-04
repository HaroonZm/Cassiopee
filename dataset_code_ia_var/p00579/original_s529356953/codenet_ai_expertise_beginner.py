from collections import deque

N, M = map(int, input().split())
A = list(map(int, input().split()))
S = []
for i in range(N):
    S.append([])
for i in range(M):
    l, r = map(int, input().split())
    S[l-1].append(r)

# Segment tree setup
size = 1
while size < N + 1:
    size *= 2
INF = 2**31 - 1
data = [INF] * (2 * size)

def update(idx, value):
    idx = idx + size - 1
    data[idx] = value
    while idx > 0:
        idx = (idx - 1) // 2
        left = 2 * idx + 1
        right = left + 1
        data[idx] = max(data[left], data[right])

def query(l, r):
    l += size
    r += size
    res = -INF
    while l < r:
        if l % 2 == 1:
            res = max(res, data[l - 1])
            l += 1
        if r % 2 == 1:
            r -= 1
            res = max(res, data[r - 1])
        l //= 2
        r //= 2
    return res

update(0, 0)
q = deque()
for i in range(N):
    while q and q[0][1] <= i:
        q.popleft()
    if q:
        r = q[0][0] + 1
    else:
        r = i + 1
    v = query(0, r) + A[i]
    update(i + 1, v)
    for rr in S[i]:
        q.append((i, rr))
print(query(0, N + 1))