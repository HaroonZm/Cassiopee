N = int(input())
S = [list(input()) for _ in range(N)]
T = [list(_) for _ in zip(*S)]
cnt = 0
for i in range(N):
    f = 1
    for j in range(N):
        if S[i + j - N] != T[j][i:] + T[j][:i]:
            f = 0
            break
    cnt += f
print(cnt * N)