N = int(input())
P = list(map(int, input().split()))

asum = [1] * (N + 1)
bsum = [-1] * (N + 1)
bsum[0] = N

for i in range(N):
    p = P[i] - 1
    asum[p + 1] += 20000 - i
    bsum[0] += 20000 - i
    bsum[p] -= 20000 - i

a = [0] * N
b = [0] * N
a[0] = asum[0]
b[0] = bsum[0]

for i in range(1, N):
    a[i] = a[i-1] + asum[i]
    b[i] = b[i-1] + bsum[i]

for i in range(N):
    print(a[i], end=' ')
print()
for i in range(N):
    print(b[i], end=' ')