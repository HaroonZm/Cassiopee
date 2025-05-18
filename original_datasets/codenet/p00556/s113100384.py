N, M = map(int, input().split())
D = [[0]*(N+1) for i in range(M)]
cnts = [0]*M
for i in range(N):
    v = int(input())
    cnts[v-1] += 1
    D[v-1][i+1] = 1
for i in range(M):
    d = D[i]
    for j in range(1, N+1):
        d[j] += d[j-1]
memo = [None]*(2**M)
memo[2**M-1] = 0
def dfs(state, idx):
    if memo[state] is not None:
        return memo[state]
    res = N
    for i in range(M):
        if state & (1 << i) == 0:
            need = cnts[i] - (D[i][cnts[i] + idx] - D[i][idx])
            res = min(res, need + dfs(state | (1 << i), idx + cnts[i]))
    memo[state] = res
    return res
print(dfs(0, 0))