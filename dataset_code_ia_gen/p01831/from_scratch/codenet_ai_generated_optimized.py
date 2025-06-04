import sys
sys.setrecursionlimit(10**7)

N = int(input())
S = input()

memo = [-1] * N

def dfs(i):
    if memo[i] != -1:
        return memo[i]
    d = S[i]
    if d == '>':
        j = i + 1
        while j < N and S[j] == '<':
            j += 1
        if j >= N:
            memo[i] = 1
            return memo[i]
        memo[i] = 1 + dfs(j)
    else:  # d == '<'
        j = i - 1
        while j >= 0 and S[j] == '>':
            j -= 1
        if j < 0:
            memo[i] = 1
            return memo[i]
        memo[i] = 1 + dfs(j)
    return memo[i]

ans = 0
for i in range(N):
    if memo[i] == -1:
        dfs(i)
    if memo[i] > ans:
        ans = memo[i]
print(ans)