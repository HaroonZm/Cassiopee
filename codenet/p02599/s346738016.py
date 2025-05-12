N, Q = map(int, input().split())
C = [int(i) for i in input().split()]

pi = [-1]*(N+1)
ps = [[] for _ in range(N+1)]
for i in range(N):
    l = pi[C[i]]
    if l != -1:
        ps[l].append(i)
    pi[C[i]] = i

qs = [[] for _ in range(N+1)]
for i in range(Q):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    qs[l].append((r, i))

bit = [0]*(N+1)

def bit_sum(idx):
    res_sum = 0
    while idx > 0:
        res_sum += bit[idx]
        idx -= idx & (-idx)
    return res_sum

def bit_add(idx, x):
    while idx <= N:
        bit[idx] += x
        idx += idx & (-idx)
    return True

ans = [0]*Q
for x in range(N-1, -1, -1):
    for y in ps[x]:
        bit_add(y, 1)
    for r, i in qs[x]:
        ans[i] = r-x+1-bit_sum(r)

for i in range(Q):
    print(ans[i])