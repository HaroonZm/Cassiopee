def generate_partitions(n, max_value=None):
    """
    再帰的にnの全ての整数の降順パーティションを生成するジェネレータ。
    各パーティションは、隣り合う列が左側が右側より低くならない（つまり降順）
    制約を満たす n の分割。

    :param n: 分割する整数
    :param max_value: パーツの最大値（これ以上の値は使わない）
    :yield: パーティションのリスト（降順）
    """
    if max_value is None or max_value > n:
        max_value = n
    if n == 0:
        # nが0になったら空リストを返すことで再帰の終端
        yield []
    else:
        # max_valueから1まで降順でパーツを選ぶ
        for i in range(max_value, 0, -1):
            if i > n:
                continue
            # iを選び、残りn - iをi以下の値で分割
            for tail in generate_partitions(n - i, i):
                # i + tail が正しい降順列になるのでyield
                yield [i] + tail


def main():
    import sys
    # 入力は複数データセット、nが0のとき終了
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        n = int(line)
        if n == 0:
            break
        # パーティションを生成し辞書順に出力
        # 生成法で既に辞書順（降順）になっている
        for partition in generate_partitions(n):
            print(' '.join(map(str, partition)))


if __name__ == "__main__":
    main()