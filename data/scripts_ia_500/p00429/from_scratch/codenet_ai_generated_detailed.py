def run_operations(n, s):
    # この関数は文字列sに対してn回操作を繰り返し実行し、最終結果を返す。
    # 操作内容：文字列を左端から順に読み、同じ数字が連続する部分を「個数+数字」の形式に変換する。
    for _ in range(n):
        result = []
        count = 1  # 連続する数字の個数
        prev = s[0]  # 比較する前の文字
        
        for i in range(1, len(s)):
            if s[i] == prev:
                count += 1
            else:
                # 異なる数字になったので、これまでの連続した数字と個数を記録
                result.append(str(count))
                result.append(prev)
                prev = s[i]
                count = 1
        # 最後の連続部分を追加
        result.append(str(count))
        result.append(prev)
        s = "".join(result)
    return s

def main():
    import sys
    # 入力は複数データセット。n=0のとき終了
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        n = line.strip()
        if n == '':
            continue
        n = int(n)
        if n == 0:
            break
        s = sys.stdin.readline().strip()
        ans = run_operations(n, s)
        print(ans)

if __name__ == "__main__":
    main()