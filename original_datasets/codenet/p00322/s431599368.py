from collections import deque
*N, = map(int, input().split())
used = set([i for i in N if i != -1])
deq = deque({i for i in range(1, 10)} - used)
C = [1, 10, 1, 100, 10, 1, -100, -10, -1]
def solve():
    res = 0
    for i in range(9):
        res += C[i] * N[i]
    return+(res == 0)

def dfs(c, rest):
    if rest == 0:
        return solve()

    if N[c] != -1:
        return dfs(c+1, rest)

    res = 0
    for i in range(rest):
        v = deq.popleft()
        N[c] = v
        res += dfs(c+1, rest-1)
        deq.append(v)
    N[c] = -1
    return res
print(dfs(0, len(deq)))