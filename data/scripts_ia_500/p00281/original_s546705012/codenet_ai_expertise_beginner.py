N, M = map(int, input().split())
ds = []
while True:
    s, t, e = map(int, input().split())
    if s == 0 and t == 0 and e == 0:
        break
    ds.append([s - 1, t - 1, e])

L = int(input())
for _ in range(L):
    b = list(map(int, input().split()))
    c = [0] * N
    for s, t, e in ds:
        c[s] += e * b[t]
    print(" ".join(str(num) for num in c))