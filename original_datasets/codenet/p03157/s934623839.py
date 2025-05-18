import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**9)

h, w = map(int, input().split())
s = [input() for _ in range(h)]

memo = [[0] * w for _ in range(h)]

dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def dfs(i, j, color):
    if not (0 <= i <= h-1 and 0 <= j <= w-1):
        return 0, 0
    if memo[i][j] == 1:
        return 0, 0
    if s[i][j] == color:
        return 0, 0
    memo[i][j] = 1
    white, black = 0, 0
    if s[i][j] == ".":
        white += 1
    else:
        black += 1
    for dx, dy in dir:
        cur_w, cur_b = dfs(i + dx, j + dy, s[i][j])
        white += cur_w
        black += cur_b
    return white, black

ans = 0
for i in range(h):
    for j in range(w):
        if s[i][j] == ".":
            white, black = dfs(i, j, "#")
        else:
            white, black = dfs(i, j, ".")

        ans += white * black

print(ans)