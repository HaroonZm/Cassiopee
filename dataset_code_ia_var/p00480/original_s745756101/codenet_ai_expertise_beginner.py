N = int(input())
a = list(map(int, input().split()))

d = []
for i in range(N-1):
    d.append([0]*21)

d[0][a[0]] = 1

for i in range(1, N-1):
    for j in range(21):
        if j + a[i] < 21:
            d[i][j] += d[i-1][j+a[i]]
        if j - a[i] >= 0:
            d[i][j] += d[i-1][j-a[i]]

print(d[N-2][a[N-1]])