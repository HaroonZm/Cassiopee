from collections import deque
N, M = map(int, input().split())
*A, = map(int, input().split())
S = [[] for i in range(N)]
for i in range(M):
    l, r = map(int, input().split())
    S[l-1].append(r)

N0 = 2**(N).bit_length()
INF = 2**31-1
data = [INF]*(2*N0)
def update(k, x):
    k += N0-1
    data[k] = x
    while k >= 0:
        k = (k - 1) // 2
        data[k] = max(data[2*k+1], data[2*k+2])
def query(l, r):
    L = l + N0; R = r + N0
    s = -INF
    while L < R:
        if R & 1:
            R -= 1
            s = max(s, data[R-1])

        if L & 1:
            s = max(s, data[L-1])
            L += 1
        L >>= 1; R >>= 1
    return s

update(0, 0)
que = deque()
for i in range(N):
    while que and que[0][1] <= i:
        que.popleft()

    r = (que[0][0] if que else i)+1
    v = query(0, r) + A[i]
    update(i+1, v)

    for r in S[i]:
        que.append((i, r))
print(query(0, N+1))