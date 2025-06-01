import sys
from math import gcd

input = sys.stdin.readline

N = int(input())
total = {}

for _ in range(N):
    a, b = map(int, input().split())
    total[a] = total.get(a, 0) + b

# 移行、ai * 2^biの形から一旦素因数2の部分だけ取り出して整理する
weight_count = {}

for a, b in total.items():
    c = a + b
    val = 1 << b
    g = gcd(c, val)
    c //= g
    val //= g
    weight_count[c] = weight_count.get(c, 0) + val

# 2の冪乗同士を整理して再び2のマルグ表現に戻す
res = []
for w in sorted(weight_count.keys()):
    count = weight_count[w]
    # countはマルグ表現なのでそのままbとして使う
    res.append((w, count))

# 同じ重さのマルグを一つにまとめて出力
for a, b in res:
    print(a, b)