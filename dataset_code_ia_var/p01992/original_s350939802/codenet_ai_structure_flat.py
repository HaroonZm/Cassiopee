from collections import deque

N = int(input())
idxs = []
for i in range(26):
    idxs.append(deque())

cs = []
for i in range(N):
    c = input()[0]
    cs.append(c)
    ci = ord(c) - ord('a')
    idxs[ci].append(i)

dp = list(range(N))
dp[0] = 0

i = 0
while i < N:
    c = cs[i]
    ci = ord(c) - ord('a')
    if i > 0:
        if dp[i] > dp[i-1] + 1:
            dp[i] = dp[i-1] + 1

    if len(idxs[ci]) < 2:
        i += 1
        continue
    idxs[ci].popleft()
    pi = idxs[ci][0]
    dp[pi] = dp[i]
    i += 1

print(dp[-1] + 1)