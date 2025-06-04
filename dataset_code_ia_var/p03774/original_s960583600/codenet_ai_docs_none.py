N, M = map(int, input().split())
a = [0] * N
b = [0] * N
c = [0] * M
d = [0] * M
for k in range(N):
    a[k], b[k] = map(int, input().split())
for l in range(M):
    c[l], d[l] = map(int, input().split())
for i in range(N):
    s = 10 ** 9
    for j in range(M):
        if s > abs(a[i] - c[j]) + abs(b[i] - d[j]):
            s = abs(a[i] - c[j]) + abs(b[i] - d[j])
            e = j + 1
    print(e)