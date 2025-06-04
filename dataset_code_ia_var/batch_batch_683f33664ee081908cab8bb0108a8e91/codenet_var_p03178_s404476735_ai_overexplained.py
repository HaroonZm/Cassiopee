import sys
# sysモジュールはPythonのシステム固有のパラメータと関数を扱う標準ライブラリです
sys.setrecursionlimit(1 << 25)  # 再帰関数の最大再帰深度を2の25乗に設定します（極めて大きな値）
readline = sys.stdin.buffer.readline  # 標準入力をバイナリモードで1行読み込む関数です。バイナリ配列でデータを得ます
read = sys.stdin.readline  # 標準入力から1行読み込み、文字列として取得します

import numpy as np  # numpyは高速な数値計算のためのライブラリです。npとしてインポートすると短く記述できます。
from functools import partial  # partialは関数の一部引数に値をあらかじめ設定するために使います。

# np.array関数に常にdtype=np.int64を渡すような新しい関数arrayを作成します
array = partial(np.array, dtype=np.int64)
# np.zeros関数に常にdtype=np.int64を渡す新しいzeros関数を作成します
zeros = partial(np.zeros, dtype=np.int64)
# np.full関数に常にdtype=np.int64を渡す新しいfull関数を作成します
full = partial(np.full, dtype=np.int64)

ra = range  # range関数をraという名前でも扱えるようにします。整数列を生成します
enu = enumerate  # enumerateはリストなどの要素にインデックスを付与するイテレータを作る関数です

# 1行を標準入力から読み取り、int型（整数型）に変換して返すa_int関数
def a_int():
    return int(read())

MOD = 10**9 + 7  # 問題でよく使われる大きな素数。計算結果の値が大きくなる場合に、この値で割った余りを取ります
INF = 2**31  # 2147483648 > 10**9 の大きな整数値。無限大のような初期値として利用します

# 標準的な便利モジュールのimport
from collections import defaultdict, Counter, deque  # defaultdict: 辞書のサブクラス、Counter: 要素のカウント、deque: 両端キュー
from operator import itemgetter, xor, add  # itemgetterでアイテムを取得, xorでビットごとの排他的論理和, addで加算
from itertools import product, permutations, combinations  # 組み合わせや順列などのイテレータ生成
from bisect import bisect_left, bisect_right  # ソート済み配列から二分探索で挿入位置を探索する
from functools import reduce  # 累積的に関数適用

# 入力文字列を一文字ずつ整数化し、np.arrayとしてKに格納
K = np.array(list(map(int, list(input()))))
# Dを整数として読み取る
D = a_int()

'''
ある数xにおいて桁の総和がDの倍数であるかを判定する問題です。
たとえば10進数の各桁の和がDで割り切れる数が欲しい場合を考えます。

dp[i, j, k]は、「Kの上からi桁までで、桁和をDで割った余りがk、jが1のときは高位部分がまだKと一致している、jが0のときはすでに一致しない数の個数」を表します。

状態遷移:
- j=0: 既にKより小さい数列
- j=1: まだ桁ごとにKの値と一致している
各遷移でdpテーブルを更新していきます。
'''

# numbaは高速化のためJITコンパイルするためのライブラリです
from numba import njit  # njitはJust-In-Timeで関数をコンパイルします

@njit('(i8[:],i8)', cache=True)  # K:配列(i8)、D:整数(i8)を引数とします。cache=Trueでコンパイルをキャッシュします
def solve(K, D):
    N = K.shape[0]  # Kの長さ（桁数）を取得します
    # dpテーブルを初期化。次元(N+1, 2, D)。int64型のゼロで初期化
    dp = np.zeros((N + 1, 2, D), dtype=np.int64)
    dp[0, 1, 0] = 1  # i=0(最初の桁), j=1(まだ一致), k=0(余りゼロ)の場合を1通りとして初期化
    for i in range(N):  # 各桁i（左からi番目）についてループ
        for k in range(D):  # 余りk(0～D-1)についてループ
            for l in range(10):  # 現在の桁に入れる数字l（0～9)についてループ
                # 既に一致が崩れた状態(j=0)の状態遷移
                # 1つ前の桁までdp[i, 0, k]から、次の桁dp[i+1, 0, (k+l)%D]へ遷移
                dp[i + 1, 0, (k + l) % D] += dp[i, 0, k]
                if l < K[i]:  # 現在桁がK[i]より小さい場合：一致していた(j=1)が崩れる
                    dp[i + 1, 0, (k + l) % D] += dp[i, 1, k]
                # MODを取ることでオーバーフロー対策
                dp[i + 1, 0, (k + l) % D] %= MOD
            # K[i]とちょうど同じ値を選択した場合（まだ一致(j=1)が続く）
            dp[i + 1, 1, (k + K[i]) % D] += dp[i, 1, k]
            #（もしMODを厳密にしたいなら：dp[i + 1, 1, (k + K[i]) % D] %= MOD）

    # 答えの計算：最終桁（N）、一致/不一致両方の場合の余りゼロの通りの総和、0を除外（-1）
    print((dp[-1, :, 0].sum() - 1) % MOD)  # 全てのパターンのうち「数0」1通りを除く

# 関数を実行
solve(K, D)