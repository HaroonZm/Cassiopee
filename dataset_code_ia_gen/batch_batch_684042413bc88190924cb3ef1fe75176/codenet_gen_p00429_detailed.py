def transform(s: str) -> str:
    """
    与えられた文字列 s に対し、指定された圧縮操作を1回実施する。
    連続した同じ数字 a が r 個続いている場合、「r+a」という文字列に置き換える。
    """
    result = []
    count = 1  # 連続している数字の個数をカウント
    for i in range(1, len(s) + 1):
        # 端または異なる文字が来たらこれまでのカウントを結果に追加
        if i == len(s) or s[i] != s[i - 1]:
            # count と数字 s[i-1] を文字列として結合
            result.append(str(count))
            result.append(s[i - 1])
            count = 1  # カウントをリセット
        else:
            count += 1
    return ''.join(result)


def main():
    """
    標準入力から複数のデータセットを読み込み、指定された回数だけ操作を繰り返す。
    n=0 の入力があれば入力終了。
    操作後の文字列を1行で出力する。
    """
    while True:
        n = input().strip()
        if not n.isdigit():
            # 空行や不正入力をスキップ
            continue
        n = int(n)
        if n == 0:
            break
        s = input().strip()
        # n回操作を繰り返す
        for _ in range(n):
            s = transform(s)
        print(s)


if __name__ == "__main__":
    main()