X = int(input())
K = int(input())
r = list(map(int, input().split()))
Q = int(input())
p = []
for i in range(Q):
    a, t = map(int, input().split())
    p.append((a, t))

N = Q
L = 0
R = Q - 1
start = 0
sign = "-"

N0 = 1
while N0 < N:
    N0 *= 2
data = [0] * (2 * N0)
INF = 0

def update(l, r, v):
    L = l + N0
    R = r + N0
    while L < R:
        if R % 2 == 1:
            R -= 1
            data[R - 1] += v
        if L % 2 == 1:
            data[L - 1] += v
            L += 1
        L //= 2
        R //= 2

def query(k):
    k += N0 - 1
    s = INF
    while k >= 0:
        s += data[k]
        k = (k - 1) // 2
    return s

q = []
for i in range(Q):
    a, t = p[i]
    p[i] = (a, t, i)

p.sort()
dic = [-1] * Q
for i in range(Q):
    a, t, idx = p[i]
    update(i, i + 1, a)
    dic[idx] = i
    q.append((t, idx, 0))

for i in range(K):
    if i == 0:
        diff = r[i]
    else:
        diff = r[i] - r[i-1]
    q.append((r[i], -1, diff))

q.sort()
ans = [0] * Q

for val, idx, c in q:
    if idx == -1:
        if sign == "-":
            update(L, R + 1, -c)
            while L < R and query(L + 1) < 0:
                L += 1
            a = query(L)
            if a < 0:
                update(L, L + 1, -a)
            start = val
            sign = "+"
        else:
            update(L, R + 1, c)
            while L < R and query(R - 1) > X:
                R -= 1
            a = query(R)
            if a > X:
                update(R, R + 1, X - a)
            start = val
            sign = "-"
    else:
        pid = idx
        idx = dic[idx]
        if sign == "-":
            if idx < L:
                res = max(query(L) - (val - start), 0)
            elif idx > R:
                res = max(query(R) - (val - start), 0)
            else:
                res = max(query(idx) - (val - start), 0)
        else:
            if idx < L:
                res = min(query(L) + (val - start), X)
            elif idx > R:
                res = min(query(R) + (val - start), X)
            else:
                res = min(query(idx) + (val - start), X)
        ans[pid] = res

for i in range(Q):
    print(ans[i])