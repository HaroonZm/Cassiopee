import statistics

N = int(input())
A = list(map(int, input().split()))

A = [a - i for i, a in enumerate(A)]

M = int(statistics.median(A))
R = []

for m in [M-2, M-1, M, M+1, M+2]:
    R.append(sum([abs(a - m) for a in A]))

print(min(R))