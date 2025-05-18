import sys
from operator import itemgetter
# gcd
from fractions import gcd
# 切り上げ，切り捨て
from math import ceil, floor
# リストの真のコピー（変更が伝播しない）
from copy import deepcopy
# 累積和。list(accumulate(A))としてAの累積和
from itertools import accumulate
# l = ['a', 'b', 'b', 'c', 'b', 'a', 'c', 'c', 'b', 'c', 'b', 'a']
# S = Counter(l)  # カウンタークラスが作られる。S=Counter({'b': 5, 'c': 4, 'a': 3})
# print(S.most_common(2))  # [('b', 5), ('c', 4)]
# print(S.keys())  # dict_keys(['a', 'b', 'c'])
# print(S.values())  # dict_values([3, 5, 4])
# print(S.items())  # dict_items([('a', 3), ('b', 5), ('c', 4)])
from collections import Counter
import math
from functools import reduce
sys.setrecursionlimit(200000)
# input関係の定義
# local only
# if not __debug__:
#     fin = open('in_1.txt', 'r')
#     sys.stdin = fin
# local only
input = sys.stdin.readline
def ii(): return int(input())
def mi(): return map(int, input().rstrip().split())
def lmi(): return list(map(int, input().rstrip().split()))
def li(): return list(input().rstrip())
def debug(*args, sep=" ", end="\n"): print("debug:", *args, file=sys.stderr, sep=sep, end=end) if not __debug__ else None
# template

H, W = mi()
S = [li() for i in range(H)]
ans = []
for i in range(H):
    for j in range(W):
        if S[i][j] == "B":
            ans.append((i, j))
        
ans.sort(key=lambda x: x[0] + x[1])
debug(ans[-1])
debug(ans[0])
tmp = abs(ans[-1][0] - ans[0][0]) + abs(ans[-1][1] - ans[0][1])
ans.sort(key=lambda x: x[0] + (W - x[1]))
debug(ans[-1])
debug(ans[0])
tmp2 = abs(ans[-1][0] - ans[0][0]) + abs(ans[-1][1] - ans[0][1])
print(max(tmp,tmp2))