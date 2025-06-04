N = int(input())
S = []
for _ in range(N):
    S.append(input())
ans = 0
k = 0
while k < N:
    f = True
    i = 0
    while i < N:
        j = i + 1
        while j < N:
            if S[i][(j + k) % N] != S[j][(i + k) % N]:
                f = False
                break
            j += 1
        if not f:
            break
        i += 1
    if f:
        ans += N
    k += 1
print(ans)