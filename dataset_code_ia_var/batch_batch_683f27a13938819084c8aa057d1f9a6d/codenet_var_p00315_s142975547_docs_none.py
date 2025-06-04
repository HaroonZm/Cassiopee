def next(N, i):
    return ((N-i-1)+N)%N

def getState(N, G, i, j):
    return G[i][j] == G[i][next(N, j)] and G[i][j] == G[next(N, i)][j] and G[i][j] == G[next(N, i)][next(N, j)]

def getInit(N, G):
    dcnt = 0
    for i in range(N//2):
        for j in range(N//2):
            if not getState(N, G, i, j):
                dcnt += 1
    return dcnt

C, N = map(int, input().split())
G = [['N' for _ in range(N)] for _ in range(N)]
for i in range(N):
    str = input()
    for j in range(N):
        G[i][j] = int(str[j])

ans = 0
dcnt = getInit(N, G)
if dcnt == 0:
    ans += 1

for i in range(C-1):
    k = int(input())
    for j in range(k):
        r, c = map(int, input().split())
        r -= 1
        c -= 1
        pre = getState(N, G, r, c)
        G[r][c] = 0 if G[r][c] == 1 else 1
        post = getState(N, G, r, c)
        if not pre and post:
            dcnt -= 1
        elif pre and not post:
            dcnt += 1
    if dcnt == 0:
        ans += 1

print(ans)