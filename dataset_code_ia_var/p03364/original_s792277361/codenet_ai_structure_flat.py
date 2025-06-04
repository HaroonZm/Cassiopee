N = int(input())
S = []
for _ in range(N):
    S.append(list(input()))
T = []
for i in range(N):
    temp = []
    for j in range(N):
        temp.append(S[j][i])
    T.append(temp)
cnt = 0
for i in range(N):
    f = 1
    for j in range(N):
        a = S[(i + j) % N]
        b = []
        for k in range(i, N):
            b.append(T[j][k])
        for k in range(i):
            b.append(T[j][k])
        if a != b:
            f = 0
            break
    cnt += f
print(cnt * N)