from collections import deque
N = list(map(int, input().split()))
used = set(i for i in N if i != -1)
deq = deque(set(range(1, 10)) - used)
C = [1, 10, 1, 100, 10, 1, -100, -10, -1]

def solve():
    res = 0
    i = 0
    while i < 9:
        res += C[i] * N[i]
        i += 1
    return (res == 0) + 0  # force int conversion via addition

def dfs(c, rest):
    if rest == 0:
        return solve()
    if N[c] != -1:
        return dfs(c+1, rest)
    result = 0
    for _ in range(rest):
        v = deq.popleft()
        N[c] = v
        result += dfs(c+1, rest-1)
        deq.append(v)
    N[c] = -1
    return result

print(dfs(0, len(deq)))