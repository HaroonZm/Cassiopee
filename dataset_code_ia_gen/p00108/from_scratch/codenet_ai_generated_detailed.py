def main():
    import sys

    for line in sys.stdin:
        n_line = line.strip()
        if n_line == '0':
            break  # 終了条件
        n = int(n_line)
        s_line = sys.stdin.readline().strip()
        S = list(map(int, s_line.split()))

        # 出現頻度操作を繰り返し、数列の不動点を見つける
        count = 0
        current = S
        while True:
            # 出現頻度を計算
            freq = {}
            for num in current:
                freq[num] = freq.get(num, 0) + 1
            # 変換結果の数列を作成
            transformed = [freq[num] for num in current]

            count += 1
            # 不動点か判定
            if transformed == current:
                # 出力
                print(count - 1)  # 最小の実行回数は不動点になる直前の回数なのでcount-1
                print(' '.join(map(str, transformed)))
                break
            else:
                current = transformed

if __name__ == "__main__":
    main()