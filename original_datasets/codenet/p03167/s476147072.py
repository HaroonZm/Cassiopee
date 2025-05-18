import math
import fractions
import bisect
import collections
import itertools
import heapq
import string
import sys
import copy
from collections import deque
sys.setrecursionlimit(10**7)
def gcd(a,b):return fractions.gcd(a,b) #最大公約数
def lcm(a,b):return (a*b) // fractions.gcd(a,b) #最小公倍数
def iin(): return int(input()) #整数読み込み
def isn(): return input().split() #文字列読み込み
def imn(): return map(int, input().split()) #整数map取得
def iln(): return list(map(int, input().split())) #整数リスト取得
def iln_s(): return sorted(iln()) # 昇順の整数リスト取得
def iln_r(): return sorted(iln(), reverse=True) # 降順の整数リスト取得
def join(l, s=''): return s.join(l) #リストを文字列に変換
def perm(l, n): return itertools.permutations(l, n) # 順列取得
def perm_count(n, r): return math.factorial(n) // math.factorial(n-r) # 順列の総数
def comb(l, n): return itertools.combinations(l, n) # 組み合わせ取得
def comb_count(n, r): return math.factorial(n) // (math.factorial(n-r) * math.factorial(r)) #組み合わせの総数
def two_distance(a, b, c, d): return ((c-a)**2 + (d-b)**2)**.5 # 2点間の距離
MOD = 10**9+7

H,W = imn()
a = [input() for _ in range(H)]
dp = [[0 for _ in range(W+1)] for _ in range(H+1)]
dp[0][0] = 1

for i in range(H):
    for j in range(W):
        if i + 1 < H and a[i+1][j] == '.': dp[i+1][j] = (dp[i+1][j] + dp[i][j]) % MOD
        if j + 1 < W and a[i][j+1] == '.': dp[i][j+1] = (dp[i][j+1] + dp[i][j]) % MOD
print(dp[H-1][W-1])