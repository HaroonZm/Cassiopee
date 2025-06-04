nmax = 10010
size = [1]*nmax
id_ = [i for i in range(nmax+1)]

def root(i):
    while i != id_[i]:
        id_[i] = id_[id_[i]]
        i = id_[i]
    return i

def unite(p, q):
    i, j = root(p), root(q)
    if i == j:
        return
    if size[i] < size[j]:
        id_[i] = j
        size[j] += size[i]
    else:
        id_[j] = i
        size[i] += size[j]

while True:
    n = int(input())
    if n == 0:
        break
    cnt = [0]*nmax
    vmax = [0]*nmax
    f = [[0,0] for _ in range(n)]
    for i in range(n):
        a, f0, b, f1 = map(int, input().split())
        f[i][0] = f0
        f[i][1] = f1
        unite(i, a)
        unite(i, b)
    for i in range(n):
        k = root(i)
        for ff in [f[i][0], f[i][1]]:
            if cnt[k] == 0 or ff > vmax[k]:
                cnt[k] = 1
                vmax[k] = ff
            elif ff == vmax[k]:
                cnt[k] += 1
    ans = 1
    for i in range(n):
        if cnt[i]:
            ans = ans * (cnt[i] >> 1) % 10007
    print(ans)