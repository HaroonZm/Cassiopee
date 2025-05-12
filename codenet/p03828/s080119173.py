N = int(input())
y = [0]*(N+1)
for i in range(1,N+1):
    M = i
    while M > 1:
        for j in range(2,M+1):
            if M%j == 0:
                M = M//j
                y[j] += 1
                break
ans = 1
for i in y:
    ans = (ans*(i+1))%(10**9+7)
print(ans)