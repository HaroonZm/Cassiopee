#!/usr/bin/env python3
#AOJ D
import sys
sys.setrecursionlimit(1000000)

po = [1<<i for i in range(10)]

def solve(n,m,p,a,b):
    a -= 1
    b -= 1
    t = list(map(int,input().split()))
    v = [[] for i in range(m)]#隣接リスト
    for _ in range(p):
        x,y,z = list(map(int,input().split()))
        x -= 1
        y -= 1
        v[x].append((y,z))
        v[y].append((x,z))
    dp = [[float("inf") for _ in range(m)] for _ in range(po[n])]#縦:馬車券の頭数,横:各都市の数
    dp[0][a] = 0
    for i in range(po[n]):
        for j in range(n):
            if i&po[j]:continue#この馬車券の頭数使用済みなら終了
            k = i|po[j]#この馬車券の頭数を使用
            for x in range(m):
                for y,z in v[x]:
                    d = dp[i][x]+z/t[j]#前回までの移動にこの馬車券を用いた場合
                    if d < dp[k][y]:#より短いなら更新
                        dp[k][y] = d
    ans = float("inf")
    for i in range(po[n]):
        if dp[i][b] < ans:#ゴール地点の最小経路を更新しながら求める
            ans = dp[i][b]
    if ans == float("inf"):#ゴールできないなら
        print("Impossible")
    else:
        print(ans)

while 1:
    n,m,p,a,b = list(map(int,input().split()))
    if n == 0:
        break
    solve(n,m,p,a,b)