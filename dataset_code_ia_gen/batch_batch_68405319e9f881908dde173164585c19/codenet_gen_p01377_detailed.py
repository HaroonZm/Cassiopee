# 問題の要約:
# 入力文字列(s)は 'i', 'w', '(', ')' からなる。
# これを文字の置き換え（追加・削除不可）だけで左右に線対称な文字列にしたい。
# 左右に線対称な文字列は再帰的に定義されている。
# 与えられたsを変更して線対称にするための最低置き換え文字数を求める。

# (左右対称の定義)
# 空文字列は左右対称
# "i" は左右対称
# "w" は左右対称
# もし x が左右対称なら
#   "i" + x + "i"
#   "w" + x + "w"
#   "(" + x + ")"
#   ")" + x + "("
# も左右対称

# 文字列長は最大10なので全探索も可能。
# DP (メモ化再帰)で文字列の区間[l:r]を左右対称にする為の最小置換回数を求める。

import sys
sys.setrecursionlimit(10**7)

s = input()

# メモ化用辞書 (l, r) -> 最小置換回数
memo = {}

# 入力文字列 s の lからr の部分列 s[l:r]
def dfs(l, r):
    # 空文字列の部分(左閉右開なので l == r が空文字列)
    if l == r:
        # 空文字列は左右対称で置換不要
        return 0
    # 文字列長1
    if r - l == 1:
        # 1文字が左右対称可能なのは 'i' or 'w'のみ
        # s[l]と'i'または'w'のどちらかに置換した後の最小回数を返す
        c = s[l]
        cost_i = 0 if c == 'i' else 1
        cost_w = 0 if c == 'w' else 1
        return min(cost_i, cost_w)
        
    # 文字列長 >= 2 の場合の処理
    # 左右対称文字列は以下のパターン:
    # "i" + x + "i"
    # "w" + x + "w"
    # "(" + x + ")"
    # ")" + x + "("
    # それぞれについて試して最小コストを求める
    
    if (l, r) in memo:
        return memo[(l,r)]
    
    res = 10**9  # 大きな数で初期化
    
    # 長さ
    length = r - l
    
    # 中間部分 x は s[l+1:r-1]
    # もし長さが2以下で中身が存在しない場合は dfs(l+1, r-1) で対応できる(空文字列も可)
    
    # 対称ペアの候補
    pairs = [('i', 'i'), ('w', 'w'), ('(', ')'), (')', '(')]
    
    for left_char, right_char in pairs:
        # 左端と右端をこれらに置換するコスト
        cost_left = 0 if s[l] == left_char else 1
        cost_right = 0 if s[r-1] == right_char else 1
        # 中間部分の置換コスト
        cost_middle = dfs(l+1, r-1)
        total_cost = cost_left + cost_right + cost_middle
        if total_cost < res:
            res = total_cost
    
    memo[(l,r)] = res
    return res

print(dfs(0,len(s)))