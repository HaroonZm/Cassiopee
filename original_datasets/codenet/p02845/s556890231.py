import sys

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

N = ir()
A = lr()
hat = [0, 0, 0]
MOD = 10 ** 9 + 7
answer = 1
for i in range(N):
    x = hat.count(A[i])
    if x == 0:
        answer = 0
    else:
        answer *= x
        j = hat.index(A[i])
        hat[j] += 1
        answer %= MOD

print(answer%MOD)
# 30