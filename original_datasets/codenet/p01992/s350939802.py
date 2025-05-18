from collections import deque

N = int(input())
idxs = [deque() for i in range(26)]
def ctoi(c):
    return ord(c) - ord('a')

cs = []
for i in range(N):
    c = input()[0]
    cs.append(c)
    ci = ctoi(c)
    idxs[ci].append(i)

dp = [i for i in range(N)]
dp[0] = 0
for i in range(N):
    c = cs[i]
    ci = ctoi(c)
    if i > 0:
        dp[i] = min(dp[i],dp[i-1]+1)

    if len(idxs[ci]) < 2: continue
    idxs[ci].popleft()
    pi = idxs[ci][0]
    dp[pi] = dp[i]
    #print(dp)

print(dp[-1] + 1)