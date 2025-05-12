N, M = map(int, input().split())
A = [input() for _ in range(N)]
B = [input() for _ in range(N)]
ans = 0
for a, b in zip(A, B):
    for aa, bb in zip(a, b):
        if aa != bb:
            ans += 1
print(ans)