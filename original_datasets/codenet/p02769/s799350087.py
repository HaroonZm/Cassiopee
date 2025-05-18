import math
from functools import reduce
from collections import deque
import sys
sys.setrecursionlimit(10**7)

# スペース区切りの入力を読み込んで数値リストにして返します。
def get_nums_l():
    return [ int(s) for s in input().split(" ")]

# 改行区切りの入力をn行読み込んで数値リストにして返します。
def get_nums_n(n):
    return [ int(input()) for _ in range(n)]

# 改行またはスペース区切りの入力をすべて読み込んでイテレータを返します。
def get_all_int():
    return map(int, open(0).read().split())

def log(*args):
    print("DEBUG:", *args, file=sys.stderr)

def inv(x):
    return pow(x, MOD-2, MOD)

def nPk(n,k):
    return kaijo[n] * inv(kaijo[n-k]) % MOD

def nCk(n,k):
    return nPk(n,k) * inv(kaijo[k])

MOD = 10**9+7

kaijo = [0] * 400020
kaijo[0] = 1
for i in range(1, len(kaijo)):
    kaijo[i] = kaijo[i-1] * i % MOD

n,k = get_nums_l()

if k >= n-1:
    print(nCk(n+n-1, n) % MOD)
    exit()

# 0人の部屋=zがk以下であるような人数の並べ方の個数

# z=0 1
# z=1 nC1 * (n-1)H1
# z=2 nC2 * (n-2)H2
# z=3 nC3 * (n-3)H3
# z   nCz * (n-z)Hz

ans = 1
for z in range(1,k+1):
    ans += nCk(n,z) * nCk(n-1, z)

print(ans%MOD)