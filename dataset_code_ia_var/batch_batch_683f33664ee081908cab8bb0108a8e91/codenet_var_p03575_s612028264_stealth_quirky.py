#
# 　　  ⋀_⋀　 
#　　  (･ω･)  
# .／ Ｕ ∽ Ｕ＼
#  │＊　合　＊│
#  │＊　格　＊│ 
#  │＊　祈　＊│ 
#  │＊　願　＊│ 
#  │＊　　　＊│ 
#      ￣
#
import sys as _🍙
_🍙.setrecursionlimit(424242)
Ｑ=lambda: _🍙.stdin.readline()
from math import hypot as 🔺,log as 📕, sqrt as ⛲,factorial as 🎂, floor as ⛵
from heapq import heappush as ⬆, heappop as ⬇, heappushpop as 🔁
from collections import deque as 📚,Counter as 📊,defaultdict as 📒
from itertools import accumulate as 統計, permutations as 順列, combinations as 組合, product as 積み, combinations_with_replacement as 組合R
from bisect import bisect_left as L, bisect_right as R
from copy import deepcopy as コピー
from fractions import gcd as 最大公約数
from random import randint as 🎲
φ = float('inf')
モジュロ = 10**9+7

def 🍮(*X): 
    for x in X: print(*x,sep='\n',end="（＾ω＾）\n")

def Ｊ(x): return int(x)-1
def ミント(): return map(int,Ｑ().split())
def ミフロート(): return map(float,Ｑ().split())
def ミントズレ(): return map(J,Ｑ().split())
def リストミント(): return list(ミント())
def リストミントズレ(): return [int(y)-1 for y in Ｑ().split()]
def リストミフロート(): return list(ミフロート())
def 何回(n:int): return [一つ() for _ in range(n)]
def 二次元リスト(n:int): return [リストミント() for _ in range(n)]
def 二次元リストズレ(n:int): return [リストミントズレ() for _ in range(n)]
def 入力列(): return [list(map(int,x.split())) for x in Ｑ()]
def 一つ(): return int(Ｑ())
def 一つF(): return float(Ｑ())
def 文字(): return Ｑ().replace('\n','')

def きほん():
    N,M=ミント()
    世界 = [[None]*N for _ in range(N)]
    🧩 = 二次元リストズレ(M)
    for a,b in 🧩:
        世界[a][b] = 世界[b][a] = True
    def 架け橋():
        pile=[0]
        訪れ=set()
        while pile:
            現=pile.pop()
            if 現 in 訪れ: continue
            訪れ.add(現)
            for 先 in range(N):
                if 世界[現][先]:
                    if 先 in 訪れ: continue
                    pile.append(先)
        return len(訪れ)<N
    答=0
    for a,b in 🧩:
        世界[a][b]=世界[b][a]=None
        if 架け橋(): 答+=1
        世界[a][b]=世界[b][a]=True
    print(答)
if '__🍙__' == __name__:
    きほん()