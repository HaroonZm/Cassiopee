import sys
sys.setrecursionlimit(10**7)

def get_input():
    return list(map(int, input().split()))

w, h = get_input()
S = []
for _ in range(h):
    row = list(map(int, input().split()))
    S.append(row)

SW = [[0]*w for _ in range(h)]
for row_idx in range(h):
    total = 0
    for col_idx in reversed(range(w)):
        total += S[row_idx][col_idx]
        SW[row_idx][col_idx] = total

def transpose(matrix):
    return list(map(list, zip(*matrix)))

S_t = transpose(S)
SH = [[0]*w for _ in range(h)]
for col_idx in range(w):
    total = 0
    for row_idx in reversed(range(h)):
        total += S[row_idx][col_idx]
        SH[row_idx][col_idx] = total

memo = {}
def dfs(x, y):
    if x == w or y == h:
        return 0
    if (x, y) in memo:
        return memo[(x, y)]
    if (x + y) % 2 == 0:
        # first player tries to maximize
        val1 = dfs(x + 1, y) - SH[y][x]
        val2 = dfs(x, y + 1) + SW[y][x]
        res = max(val1, val2)
    else:
        # second player tries to minimize
        val1 = dfs(x + 1, y) - SH[y][x]
        val2 = dfs(x, y + 1) + SW[y][x]
        res = min(val1, val2)
    memo[(x, y)] = res
    return res

print(abs(dfs(0, 0)))