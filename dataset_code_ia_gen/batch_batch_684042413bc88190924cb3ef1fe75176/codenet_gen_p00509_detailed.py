import sys
import math

def is_prime(num: int) -> bool:
    """Check if a number is prime using deterministic Miller-Rabin for 64-bit integers."""
    if num < 2:
        return False
    # small primes to check divisibility quickly
    small_primes = [2,3,5,7,11,13,17,19,23]
    for sp in small_primes:
        if num == sp:
            return True
        if num % sp == 0 and num != sp:
            return False

    # Miller-Rabin test implementation for 64-bit integers with fixed bases
    def miller_rabin_test(a, d, n, r):
        x = pow(a, d, n)
        if x == 1 or x == n-1:
            return True
        for _ in range(r-1):
            x = (x * x) % n
            if x == n-1:
                return True
        return False

    # n-1 = d * 2^r decomposition
    d = num -1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1

    # Deterministic bases for testing 64-bit numbers from research
    test_bases = [2,325,9375,28178,450775,9780504,1795265022]
    for a in test_bases:
        if a % num == 0:
            return True
        if not miller_rabin_test(a, d, num, r):
            return False
    return True

def main():
    # 入力読み込み
    input_line = sys.stdin.readline().strip()
    n, c = input_line.split()
    n = int(n)
    c = int(c)

    # 問題文より、b1～bn, gn～g1を決める
    # b1 = g1 = 9固定、bi・gi (i=2..n) を0~9で決定
    # cは先生の中央旗 0~9 or -1(なし)
    # 並び順：
    # b1 b2 ... bn c g_n ... g2 g1  または
    # b1 b2 ... bn g_n ... g2 g1 (cなしのとき)
    #
    # b1=9, g1=9, 解は b_i,g_i (i=2..n) を探索し、
    # 旗はbiとgiは同じ数字（ペア条件）
    #
    # 0で始まる並びは禁止
    # 中央のcは先生の旗、ない場合は順番短い (2nか2n+1桁)
    #
    # 数字を整数とみなして素数判定。両チームの判定が必要だが、
    # 問題は一クラスの最強列なので当クラスが勝つ（負けない）配列を出力する。
    #
    # 今回一クラスのみなので、最大になる素数を探し、
    # 素数なら勝ち、そうでなくても最大値を狙う。

    # 両クラス等の判定は問題文に記述あるが、多分他クラスはなしで最大素数探し
    # 入力cが0~9 または -1(先生無し)

    # 制約
    # n <= 10であり、探索空間は 10^(n-1) (bi,g_iの数字 0..9)
    # 最大1e9の探索で(9桁まで)は厳しいので工夫が必要

    # 探索手法：
    # b1=9, g1=9は固定
    # b2..bn, g2..gn 各ペアは同じ数字 (0~9)
    # 中央cは-1無 or 0~9
    #
    # 数列は
    # b1 b2 ... bn (c) g_n ... g2 g1

    # 0禁止：先頭はb1=9なので大丈夫

    # 探索範囲は 10^(n-1) の並び (b2..bn の数字)
    # 同じ数字が gi に対応
    #
    # 制約は n 最大10 → b2..b10計9桁探索 → 10^9通りで完全探索は不可
    #
    # しかし、筆者が知る問題の性質上、
    # b2..bn, g2..gn は同じ数字なので探索は1つの配列

    # アプローチ
    #
    # 1. b1=9, g1=9固定
    # 2. b2..bnを全検索は大変なので、以下戦略
    # - nが小さい場合は全探索（n=1は楽）
    # - nが大きい場合は、数字を大きくして素数判定チェックし、
    # 末尾が奇数になる数字にして素数を見つけるための工夫が必要
    #
    # 公式解析は不明なので、
    # 時間制約なしで動く実装としては、n<=10まで全探索は無理なので
    # nが大きい場合は簡単なヒューリスティックで最大値を生成して判定

    # 解決策: 全探索して最大の素数を探しつつ、
    # 見つからなければ最大数を素数判定し最も大きい数を出す。

    # 各数字でループして最大を記録する上で効率は考慮しつつ、
    # できるだけ高速化するため、メモ化や素数判定も高速に。

    # まず必要な関数を作成
    # 次にb2..bnを再帰的に決めていく
    # 出力ルールは1案(先生有or無)を判別し全探索

    # 先生いる時の桁数は2n+1、いないと2n桁

    # 大きい順に探索し、最初に発見した素数を出力し終了

    # いいねー、最大値を優先して探索しよう

    # b1=9固定ということは、b2..bnは9から0にかけて試す

    # 実装開始

    # 使用する構造: 再帰でb2..bn決めていく(上から最大探索)
    # cが-1でないならcは固定
    # 数の文字列構築：
    # b1 b2 ... bn (c if exists) g_n ... g2 g1
    #    ９  b2...bn           g_n...g2    ９

    # 先生無の場合は cが無し

    # 先生いるあり、b2..bnを決めて、それが決まったら、最終文字列作成して素数判定

    # 実装時は、b2..bnをリストとし呼び出し最大値記憶

    # 先にb2..bnの最大数優先で探索

    # 大域変数で最大素数と最大数管理

    max_prime = -1
    max_prime_str = ""
    max_num = -1
    max_num_str = ""

    b1 = 9
    g1 = 9

    # 再帰探索
    def dfs(pos, b_arr):
        """
        pos : 現在決めているペア(2..n)
        b_arr: 現在決定済みのb2..b_pos-1
        """
        nonlocal max_prime, max_prime_str, max_num, max_num_str

        if pos == n+1:
            # 全b2..bn決定
            # 文字列組み立て
            # b1 b2..bn
            # c or not
            # gn .. g2 g1 (=b1..bnを逆順)
            # 各ペアの女子は男子と同じ数字
            # g_i = b_i

            # b_list: [b1] + b_arr
            b_list = [b1] + b_arr  # length n

            # g_list = b_list reversed
            g_list = b_list[::-1]

            # cの有無セット
            if c >= 0:
                # cあり
                digits = b_list + [c] + g_list
            else:
                digits = b_list + g_list

            # 先頭0チェック（b1は9なので問題なし）

            # 末尾に0チェックは禁止されてない問題文より。問題文は先頭の0は禁止だけ
            # ここでは先頭はb1=9なので問題なし。

            num_str = ''.join(str(d) for d in digits)
            num_int = int(num_str)

            # 最大数の更新候補に入れる
            if num_int > max_num:
                max_num = num_int
                max_num_str = num_str

            # 素数判定
            if is_prime(num_int):
                # 素数なら最大素数更新検討
                if num_int > max_prime:
                    max_prime = num_int
                    max_prime_str = num_str
            return

        # pos < n+1 の時
        # b_i を 9..0 で試す（大きい数字優先）
        for d in range(9,-1,-1):
            # b_arr に d足して次へ
            dfs(pos+1, b_arr + [d])

    # n=1特別ケースでも普通に動く前提
    # 探索開始
    dfs(2, [])

    # 素数見つかればそれを出力、なければ最大数を出力
    if max_prime_str != "":
        print(max_prime_str)
    else:
        print(max_num_str)
    # 改行はprintの最後で出る

if __name__ == "__main__":
    main()