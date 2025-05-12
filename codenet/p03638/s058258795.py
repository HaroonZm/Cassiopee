H, W = map(int, input().split())
N = int(input())
A = list(map(int, input().split()))

path = []
for i in range(H):
    if i % 2 == 0:
        range_ = range(W)
    else:
        range_ = reversed(range(W))
    for j in range_:
        path.append((i, j))

c = []
for i, a in enumerate(A):
    for j in range(a):
        c.append(i+1)

ans = [[0]*W for _ in range(H)]
for k, p in enumerate(path):
    i, j = p
    ans[i][j] = c[k]

for elem in ans:
    print(' '.join(map(str, elem)))