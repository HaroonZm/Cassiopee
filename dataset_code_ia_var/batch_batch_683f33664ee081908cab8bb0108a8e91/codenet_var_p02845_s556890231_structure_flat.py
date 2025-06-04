import sys

N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split()))
hat = [0, 0, 0]
MOD = 10 ** 9 + 7
answer = 1
for i in range(N):
    cnt = 0
    for h in hat:
        if h == A[i]:
            cnt += 1
    if cnt == 0:
        answer = 0
    else:
        answer *= cnt
        for j in range(3):
            if hat[j] == A[i]:
                hat[j] += 1
                break
        answer %= MOD

print(answer % MOD)