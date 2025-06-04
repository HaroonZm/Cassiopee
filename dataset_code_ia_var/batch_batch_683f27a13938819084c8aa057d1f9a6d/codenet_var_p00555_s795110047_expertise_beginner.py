N, M, D = map(int, input().split())
S = []
for i in range(N):
    row = list(input())
    S.append(row)

ans = 0

# Vérifier les lignes
for i in range(N):
    count = 0
    for j in range(M):
        if S[i][j] == ".":
            count = count + 1
            if count >= D:
                ans = ans + 1
        else:
            count = 0

# Vérifier les colonnes
for j in range(M):
    count = 0
    for i in range(N):
        if S[i][j] == ".":
            count = count + 1
            if count >= D:
                ans = ans + 1
        else:
            count = 0

print(ans)