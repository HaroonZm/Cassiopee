# このプログラムは、ハミング数（2, 3, 5のみを素因数に持つ数）を1から1000000まで事前に生成し、
# 入力される範囲[m, n]の中にあるハミング数の個数を効率よく数えるために、
# 事前計算＋二分探索を用いた方法を採用しています。

import sys
import bisect

def generate_hamming_numbers(limit):
    # ハミング数を生成するための集合。初期値は1。
    hamming = set([1])
    # 新たに発見した数を展開するためのリスト
    queue = [1]
    # 素因数候補
    factors = [2, 3, 5]

    for num in queue:
        for f in factors:
            next_num = num * f
            # limit以下の数だけ追加する
            if next_num <= limit and next_num not in hamming:
                hamming.add(next_num)
                queue.append(next_num)
    # ソートしてリストとして返す
    return sorted(hamming)

def main():
    # 入力範囲は最大1000000なので、この範囲のハミング数を事前に生成
    limit = 10**6
    hamming_numbers = generate_hamming_numbers(limit)

    # 標準入力を一行ずつ読み込む
    for line in sys.stdin:
        line = line.strip()
        # 終了条件の "0" のみの行
        if line == "0":
            break
        m, n = map(int, line.split())

        # m以上の最初のハミング数の位置を二分探索で取得
        left = bisect.bisect_left(hamming_numbers, m)
        # n以下の最後のハミング数の位置を二分探索で取得(右側の境界の次の位置)
        right = bisect.bisect_right(hamming_numbers, n)

        # [m, n]の範囲内のハミング数の個数はright - left
        print(right - left)

if __name__ == "__main__":
    main()