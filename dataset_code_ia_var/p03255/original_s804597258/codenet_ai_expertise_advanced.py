from itertools import accumulate

def E(i, x):
    return (5 if i == 1 else 2 * i + 1) * x

N, X = map(int, input().split())
G = sorted(map(int, input().split()), reverse=True)
accG = [0, *accumulate(G)]
min_ans = float('inf')

for k in range(1, N + 1):
    now = 0
    for i in range(1, (N + k - 1)//k + 1):
        l, r = (i - 1) * k, min(i * k, N)
        now += E(i, accG[r] - accG[l])
    min_ans = min(min_ans, now + (N + k) * X)

print(min_ans)