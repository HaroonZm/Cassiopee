import sys
n, m = [int(i) for i in sys.stdin.readline().split()]
graph = {i : [] for i in range(n)}
INF = 10 ** 18
for i in range(m):
    a, b = [int(i) for i in sys.stdin.readline().split()]
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)

# memo_ls[i][j] 状態iでjにいる時の通り数
memo_ls = [[-1 for j in range(n)] for i in range(1 << n)]
# 状態sでvにいる通り数
def bit_dp(s, v):
    if memo_ls[s][v] >= 0:
        return memo_ls[s][v]
    if s == (1 << n) - 1:
        return 1
    res = 0
    for i in graph[v]:
        already = s >> i
        if not (already & 1):
            res += bit_dp((s | (1 << i)), i)
    memo_ls[s][v] = res
    return res

res = bit_dp(1, 0)
print(res)