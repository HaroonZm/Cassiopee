import sys
import math
sys.setrecursionlimit(10**7)

n, c = map(int, sys.stdin.readline().split())

# 素数判定（ミラーラビン素数判定法）
def is_prime(n):
    if n < 2:
        return False
    for p in [2,3,5,7,11,13,17,19,23]:
        if n == p:
            return True
        if n % p == 0 and n != p:
            return False
    d = n -1
    r = 0
    while d % 2 == 0:
        d >>= 1
        r += 1
    for a in [2,3,5,7,11]:
        if a >= n:
            break
        x = pow(a,d,n)
        if x == 1 or x == n -1:
            continue
        for _ in range(r-1):
            x = (x*x) % n
            if x == n -1:
                break
        else:
            return False
    return True

# 与えられた数字列が先頭ゼロ禁止条件を満たしているか
def valid_start(s):
    return s[0] != '0'

# 配列を文字列に変換
def arr_to_str(arr):
    return ''.join(map(str, arr))

# 先生が居る場合と居ない場合、2ケースで処理
# 基本は男子bは昇順、女子gは降順（ペアなので同じ数字）
# 関数生成
# "b1 b2 ... bn c gn ... g2 g1" または "b1 b2 ... bn gn ... g2 g1"
# bは昇順数字配列形にする
# gはbと同じだが順番逆
# cがあるなら間に挟む

# 男子の並びを決める。条件は先頭ゼロ禁止なので、b1≠0
# 女子は必ずbの逆順（数字同じ）なので決まる

# 与えられる旗は何でもよいので男子の数字配列を決めればOK
# 勝利条件は
# ・数が素数なら勝ち、両方素数なら大きい方勝ち、両方非素数なら大きい方勝ち

# nは最大10なので最大20または21桁の数字を生成可能
# 最適解を求める手法:
# - 先生が居る場合: 2n+1桁の数字
# - 先生が居ない場合: 2n桁の数字
# 一番大きい数字になる配列から順に試せばよい
# ただしこのままだと10!は36,288,000で大きすぎ

# 最適化策:
# - 先頭数字はb1>0で定まっている
# - b全体は男子の旗であるため、男の旗は何でも自由に選べる
# →最適はbをできるだけ大きく、女子は逆順
# ↓より大きくするため各bは9に近い値を入れるべき
# ただしすべて9にすると大きいが素数にならない可能性高いので数字を調整

# 効率的な解法:
# nは最大10で組み合わせ探索は厳しいので、貪欲に上から数字を決め、
# 柔軟に値を変えて、素数条件を満たす最大の数字を作成する。

# 具体的手順:
# bは長さnの整数配列、初期値は9で全埋め
# cは固定（もしc>=0なら間に入る）
# 答えは b + [c] + g, gはbの逆順
# 数が素数か判定する
# 素数でなければ小さい順に数字を減らし、素数を探す
# 先頭が0は禁止
# 男女のそれぞれの位置の数字は同じなのでb[i]とg[i]は一致
# つまりbの数字を調節すれば良い

# 探索空間が大きい：
# 9^nは爆発的に大きすぎる
# n=10では10**9超
# よって単に全探索は不可

# 最適化：
# 降順に試す。先頭b1は1~9、次は0~9以下で徐々に減らす
# 順列ではなく順列の列、bを桁の数字と考え、数字列を生成し、
# 大きい数字から試すため、bを高い数字から順に決定していく再帰探索

# さらに途中でprune（剪定）を入れる
# - 先頭数字が0なら中止
# - 途中で探索できなければ中止

# 早期終了を念頭に置き、上から決めていく実装

from functools import lru_cache

length = 2 * n + (1 if c >= 0 else 0)

# 与えられたb配列から候補文字列作成
def build_number(b):
    if c >= 0:
        return arr_to_str(b) + str(c) + arr_to_str(b[::-1])
    else:
        return arr_to_str(b) + arr_to_str(b[::-1])

# 先頭数字0禁止
def check_start(s):
    return s[0] != '0'

# bを数字のリストとする再帰的全探索(深さ優先)。先頭の数字から決定
# 大きい数字から試すために9から0に向けて試行
# 途中でpruneで絞る

# 返り値は最良のb配列かNone

def dfs(pos, b):
    if pos == n:
        s = build_number(b)
        if not check_start(s):
            return None
        num = int(s)
        if is_prime(num):
            return b
        return None
    start_digit = 9
    # 探索
    for d in range(9, -1, -1):
        # 先頭，0禁止
        if pos == 0 and d == 0:
            continue
        b[pos] = d
        res = dfs(pos+1, b)
        if res is not None:
            return res
    return None

b = [0]*n
res = dfs(0, b)

# もし素数解が見つからなければ素数にこだわらず最大の数字を出す
# つまり最大のb=[9]*n（先頭に0禁止のため先頭は9）で出す
# 先生いるケースといないケースで構築

if res is None:
    b = [9]*n
    if b[0] == 0:
        for d in range(9,0,-1):
            b[0] = d
            break
    res = b

print(build_number(res))