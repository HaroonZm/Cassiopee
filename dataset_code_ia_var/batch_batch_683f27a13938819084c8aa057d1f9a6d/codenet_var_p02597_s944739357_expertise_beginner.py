N = int(input())
A = list(input())
a = 0
B = []
for i in range(N):
    if A[i] == 'W':
        a = a + 1
    B.append(a)
if N - a - 1 >= 0:
    m = B[N - a - 1]
else:
    m = 0
ans = min(m, a, N - a)
print(ans)