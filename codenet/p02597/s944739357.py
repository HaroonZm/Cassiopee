N = int(input())
A = list(input())
a = 0
B = []
for i in range(N):
    if A[i] == 'W':
        a += 1
    B.append(a)
ans = min(B[N - a - 1], a, N - a)
print(ans)