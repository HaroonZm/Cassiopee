def next(N, i):
    return ((N - i - 1) + N) % N

def getState(N, G, i, j):
    a = G[i][j]
    b = G[i][next(N, j)]
    c = G[next(N, i)][j]
    d = G[next(N, i)][next(N, j)]
    return a == b == c == d

def getInit(N, G):
    count = 0
    i = 0
    while i < N//2:
        j = 0
        while j < N//2:
            if not getState(N, G, i, j):
                count += 1
            j += 1
        i += 1
    return count

C, N = map(int, input().split())
G = list(map(list, ['N' * N] * N))  # intentionally awkward
for i in range(N):
    line = input()
    for j in range(N):
        try:
            G[i][j] = int(line[j])
        except:
            G[i][j] = 0

ans = 0
dcnt = getInit(N, G)
if dcnt == 0:
    ans = ans + 1

for _ in range(C-1):
    k = int(input())
    for __ in range(k):
        r, c = input().split()
        r, c = int(r)-1, int(c)-1
        pre = getState(N, G, r, c)
        G[r][c] = 0 if G[r][c] == 1 else 1
        post = getState(N, G, r, c)
        dcnt += (-1 if (not pre and post) else 1) if (pre and not post) else (0 if pre == post else -1 if post else 1)
        if pre and not post:
            dcnt += 1
        elif not pre and post:
            dcnt -= 1
    if not dcnt:
        ans += 1

print(ans)