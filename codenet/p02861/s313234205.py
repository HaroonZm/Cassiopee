#むちゃくちゃ大事
#街の数を受け取り、その経路の平均値を求めるプログラム

import numpy as np

import math

#街の数を受けとる
n = int(input())

#街の位置ベクトルを保存するためのリスト
a = []

#合計値
sum = 0

#街の一ベクトルを取得
for i in range(n):
    a.append(np.array(list(map(int,input().split()))))

for i in range(n):
    for s in range(i,n):
        sum += np.linalg.norm(a[s] - a[i])

#平均値を表示 sum : 経路の合計  math.factorial(n) : nの階乗
print(sum*2/n)