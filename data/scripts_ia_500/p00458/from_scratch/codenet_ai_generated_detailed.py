import sys
sys.setrecursionlimit(10**7)

# 再帰的に深さ優先探索(DFS)で、指定区画からの最大移動区画数を求める関数
def dfs(i, j):
    # もしすでにdpに値があれば再計算しない（メモ化）
    if dp[i][j] != -1:
        return dp[i][j]
    # 現在位置の最大移動区画数は最低1（自分自身の区画）
    dp[i][j] = 1
    for di, dj in directions:
        ni, nj = i + di, j + dj
        # 範囲内かつ薄氷がある区画かどうか確認
        if 0 <= ni < n and 0 <= nj < m and ice[ni][nj] == 1:
            # まだ割っていない薄氷の区画への移動なので、次の区画の最大移動区画数も調べる
            dp[i][j] = max(dp[i][j], 1 + dfs(ni, nj))
    return dp[i][j]

while True:
    m = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    if m == 0 and n == 0:
        break
    ice = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    # dp配列は-1で初期化し未計算状態を表す
    dp = [[-1]*m for _ in range(n)]
    # 移動方向は東西南北
    directions = [(1,0),(-1,0),(0,1),(0,-1)]
    ans = 0
    # 薄氷があるすべての区画からDFSを始めて最大値を探す
    for i in range(n):
        for j in range(m):
            if ice[i][j] == 1:
                ans = max(ans, dfs(i,j))
    print(ans)