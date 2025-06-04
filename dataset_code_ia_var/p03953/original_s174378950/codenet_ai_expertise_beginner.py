import sys

sys.setrecursionlimit(10 ** 7)

N = int(sys.stdin.readline())
X = list(map(int, sys.stdin.readline().split()))
M, K = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

P = list(range(N))
for a in A:
    tmp = P[a - 1]
    P[a - 1] = P[a]
    P[a] = tmp

def my_power(P, n):
    if n == 1:
        return P[:]
    Q = my_power(P, n // 2)
    R = [Q[q] for q in Q]
    if n % 2 == 1:
        return [P[r] for r in R]
    else:
        return R

Q = my_power(P, K)

diff = [X[0]]
for i in range(1, N):
    diff.append(X[i] - X[i - 1])

answer = []
total = 0
for idx in Q:
    total += diff[idx]
    answer.append(str(total))

print('\n'.join(answer))