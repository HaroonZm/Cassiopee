N = int(input())
y = [0]*(N+1)
i = 1
while i <= N:
    M = i
    while M > 1:
        j = 2
        while j <= M:
            if M % j == 0:
                M = M // j
                y[j] += 1
                break
            j += 1
    i += 1
ans = 1
i = 0
while i < len(y):
    ans = (ans * (y[i] + 1)) % (10**9 + 7)
    i += 1
print(ans)