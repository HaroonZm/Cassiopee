import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

H, W = map(int, input().split())
M = [list(map(int, input().split())) for _ in range(H)]

# directions: up, down, left, right
dirs = [(-1,0), (1,0), (0,-1), (0,1)]

# メモ変数: memo[i][j]は(i,j)領域に水が溜まる区域の候補をビット集合で表す
# ここでは、領域番号を1次元で管理するために0~H*W-1で番号付ける
memo = [None]*(H*W)

def idx(i,j):
    return i*W + j

def rev_idx(v):
    return divmod(v, W)

def dfs(i,j):
    v = idx(i,j)
    if memo[v] is not None:
        return memo[v]
    lower_neighbors = []
    for dx, dy in dirs:
        ni, nj = i+dx, j+dy
        if 0 <= ni < H and 0 <= nj < W:
            if M[ni][nj] < M[i][j]:
                lower_neighbors.append((ni,nj))
    if not lower_neighbors:
        # 自分自身に水が溜まる
        memo[v] = 1 << v
        return memo[v]
    result = 0
    for ni,nj in lower_neighbors:
        result |= dfs(ni,nj)
    memo[v] = result
    return result

count = 0
for i in range(H):
    for j in range(W):
        res = dfs(i,j)
        # resに含まれるビットの数が2以上なら尾根
        # ビットカウント
        if bin(res).count('1') >= 2:
            count += 1

print(count)