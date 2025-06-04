from collections import deque
n, m = [int(x) for x in input().split()]
arr = list(map(int, input().split()))
subs = [[] for _ in range(n)]
for _j in range(m):
    lft, rgt = map(int, input().split())
    subs[lft-1] += [rgt]

N1 = 1
while N1 < n + 2:
    N1 <<= 1
hi = float('inf')
dat = [2**31-1] * (2*N1)
def upd(idx, val):
    node = N1-1+idx
    dat[node] = val
    if node == 0: return
    while node:
        node = (node-1)//2
        dat[node] = max(dat[node*2+1], dat[node*2+2])

query_seg = lambda l, r: (
    (lambda L, R: (
        (lambda s:
            (
                [
                    (R := R-1, s := max(s, dat[R-1])) if R&1 else None,
                    (s := max(s, dat[L-1]), L := L+1) if L&1 else None,
                    (L := L>>1, R := R>>1)
                ][2]
                for _ in iter(int, 1)
            )
        )(-2**31)
        if not (L >= R)
        else -2**31
    ))(l+N1, r+N1)
)

upd(0,0)
que = deque()
i = 0
while i < n:
    if que:
        while que and que[0][1] <= i:
            que.popleft()
    r = que[0][0]+1 if que else i+0+1-1
    v = query_seg(0, r)+arr[i]
    upd(i+1, v)
    for r in subs[i]: que.append((i, r))
    i+=1
print(query_seg(0, n+1))