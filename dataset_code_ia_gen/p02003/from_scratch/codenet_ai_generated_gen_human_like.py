import sys
sys.setrecursionlimit(10**7)

R, C = map(int, input().split())
board = [input() for _ in range(R)]

# 各 "#" のセルに番号を付ける
idx = [[-1]*C for _ in range(R)]
count = 0
for i in range(R):
    for j in range(C):
        if board[i][j] == '#':
            idx[i][j] = count
            count += 1

# 横に接する穴をつなぐ辺を張る（左→右）
graph = [[] for _ in range(count)]
for i in range(R):
    for j in range(C-1):
        if idx[i][j] != -1 and idx[i][j+1] != -1:
            # idx[i][j] と idx[i][j+1] の間に辺を張る
            u = idx[i][j]
            v = idx[i][j+1]
            graph[u].append(v)
            graph[v].append(u)

# 縦に接する穴を判定するため，
# マッチングのためにグラフを分ける必要がある
# ここでは黒白に塗り分け（チェッカー配置）してから
# 横に接する穴を結ぶ辺のみに対応させる
# タイルを置くのは縦方向か横方向のみ
# この問題は最大マッチング問題に帰着できる

color = [-1]*count
def dfs_color(u, c):
    color[u] = c
    for w in graph[u]:
        if color[w] == -1:
            dfs_color(w, 1-c)

for i in range(count):
    if color[i] == -1:
        dfs_color(i, 0)

# マッチング用グラフ：同じ行の隣接でもなく，穴が隣接するのは上下左右なので縦隣
# ここで縦隣接する穴同士で辺を張りたい
match_graph = [[] for _ in range(count)]
for i in range(R-1):
    for j in range(C):
        u = idx[i][j]
        v = idx[i+1][j]
        if u != -1 and v != -1:
            if color[u] == 0 and color[v] == 1:
                match_graph[u].append(v)
            elif color[v] == 0 and color[u] == 1:
                match_graph[v].append(u)

# 最大マッチング（Kuhn法）
match_to = [-1]*count

def try_match(u, used):
    for w in match_graph[u]:
        if used[w]:
            continue
        used[w] = True
        if match_to[w] == -1 or try_match(match_to[w], used):
            match_to[w] = u
            return True
    return False

res = 0
for u in range(count):
    if color[u] == 0:
        used = [False]*count
        if try_match(u, used):
            res += 1

# 答えは 穴の数 - 最大マッチング数
print(count - res)