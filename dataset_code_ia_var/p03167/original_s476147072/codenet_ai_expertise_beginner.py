import sys

MOD = 10**9 + 7

# 関数(簡単版)
def read_int():
    return int(input())

def read_ints():
    return map(int, input().split())

def read_list():
    return list(map(int, input().split()))

# グリッドサイズの取得
H, W = map(int, input().split())

# グリッド読み込み
a = []
for _ in range(H):
    a.append(input())

# dp配列の初期化 (1つ大きめにとる)
dp = []
for i in range(H+1):
    row = []
    for j in range(W+1):
        row.append(0)
    dp.append(row)

dp[0][0] = 1

# dp計算
for i in range(H):
    for j in range(W):
        if i+1 < H and a[i+1][j] == '.':
            dp[i+1][j] = (dp[i+1][j] + dp[i][j]) % MOD
        if j+1 < W and a[i][j+1] == '.':
            dp[i][j+1] = (dp[i][j+1] + dp[i][j]) % MOD

print(dp[H-1][W-1])