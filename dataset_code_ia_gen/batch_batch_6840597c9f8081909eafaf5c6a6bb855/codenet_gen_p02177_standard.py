N,M = map(int, input().split())
implication = [[False]*N for _ in range(N)]
for i in range(N):
    implication[i][i] = True
for _ in range(M):
    a,b = map(int, input().split())
    implication[a-1][b-1] = True
for k in range(N):
    for i in range(N):
        if implication[i][k]:
            for j in range(N):
                if implication[k][j]:
                    implication[i][j] = True
for i in range(N):
    equiv = [j+1 for j in range(N) if implication[i][j] and implication[j][i]]
    print(*equiv)