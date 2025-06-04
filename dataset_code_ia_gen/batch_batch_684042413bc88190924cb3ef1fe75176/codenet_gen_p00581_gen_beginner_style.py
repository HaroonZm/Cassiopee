H, W = map(int, input().split())
S = [input() for _ in range(H)]

count = 0
for i in range(H):
    for j in range(W):
        if S[i][j] == 'J':
            for k in range(i+1, H):
                for l in range(j+1, W):
                    if S[i][l] == 'O' and S[k][j] == 'I':
                        count += 1

print(count)