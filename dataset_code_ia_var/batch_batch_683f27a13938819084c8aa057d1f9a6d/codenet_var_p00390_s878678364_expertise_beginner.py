N = int(input())
A = list(map(int, input().split()))
W = list(map(int, input().split()))

INF = 10 ** 9
l = INF
r = INF

for i in range(N):
    a = A[i]
    w = W[i]
    if a == 1:
        if w < r:
            r = w
    else:
        if w < l:
            l = w

if l == INF or r == INF:
    print(0)
else:
    print(l + r)