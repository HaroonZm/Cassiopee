N, K = map(int, input().split())

Sunuke = [1] * N
for i in range(K):
    d = int(input())
    A = list(map(int, input().split()))
    for ii in range(d):
        Sunuke[A[ii] - 1] = 0

print(sum(Sunuke))